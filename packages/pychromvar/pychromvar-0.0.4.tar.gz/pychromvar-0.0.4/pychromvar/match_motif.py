import os
import numpy as np
import scipy as sp
from typing import Union, Literal, get_args
from tqdm import tqdm
import MOODS.scan
import MOODS.tools
from anndata import AnnData
from mudata import MuData

_BACKGROUND = Literal["subject", "genome", "even"]


def match_motif(data: Union[AnnData, MuData], motifs, pseudocounts=0.0001, p_value=5e-05,
                background: _BACKGROUND = "even", genome_file: str = None):
    """Perform motif matching to predict binding sites using MOODS. 

    Parameters
    ----------
    data : Union[AnnData, MuData]
        AnnData object with peak counts or MuData object with 'atac' modality.
    motifs : _type_
        List of motifs
    pseudocounts : float, optional
        Pseudocounts for each nucleotide, by default 0.0001
    p_value : _type_, optional
        _description_, by default 5e-05
    background : _BACKGROUND, optional
        Background distribution of nucleotides for computing thresholds from p-value. 
        Three options are available: "subject" to use the subject sequences, "genome" to use the
        whole genome (need to provide a genome file), or even using 0.25 for each base, by default "even"
    genome_file : str, optional
        If background is set to genome, a genome file must be provided, by default None

    Returns
    -------
    Update data.
    """

    if isinstance(data, AnnData):
        adata = data
    elif isinstance(data, MuData) and "atac" in data.mod:
        adata = data.mod["atac"]
    else:
        raise TypeError(
            "Expected AnnData or MuData object with 'atac' modality")

    assert "peak_seq" in adata.uns_keys(), "Cannot find sequences, please first run add_peak_seq!"

    options = get_args(_BACKGROUND)
    assert background in options, f"'{background}' is not in {options}"

    if background == "genome":
        assert os.path.exists(genome_file), f"{genome_file} does not exist!"

    # add motif names to Anndata object
    adata.uns['motif_name'] = [None] * len(motifs)
    for i in range(len(motifs)):
        adata.uns['motif_name'][i] = motifs[i].matrix_id + "." + motifs[i].name

    # compute background distribution
    seq = ""
    if background == "subject":
        for i in range(adata.n_vars):
            seq += adata.uns['peak_seq'][i]
        bg = MOODS.tools.bg_from_sequence_dna(seq, 0)
    elif background == "genome":
        # TODO
        bg = MOODS.tools.flat_bg(4)
    else:
        bg = MOODS.tools.flat_bg(4)

    # prepare motif data
    n_motifs = len(motifs)

    matrices = [None] * 2 * n_motifs
    thresholds = [None] * 2 * n_motifs
    for i, motif in enumerate(motifs):
        counts = (tuple(motif.counts['A']),
                  tuple(motif.counts['C']),
                  tuple(motif.counts['G']),
                  tuple(motif.counts['T']))

        matrices[i] = MOODS.tools.log_odds(counts, bg, pseudocounts)
        matrices[i+n_motifs] = MOODS.tools.reverse_complement(matrices[i])

        thresholds[i] = MOODS.tools.threshold_from_p(matrices[i], bg, p_value)
        thresholds[i+n_motifs] = thresholds[i]

    # create scanner
    scanner = MOODS.scan.Scanner(7)
    scanner.set_motifs(matrices=matrices, bg=bg, thresholds=thresholds)
    adata.varm['motif_match'] = np.zeros(shape=(adata.n_vars, n_motifs), dtype=np.uint8)

    for i in tqdm(range(adata.n_vars)):
        results = scanner.scan(adata.uns['peak_seq'][i])
        for j in range(n_motifs):
            if len(results[j]) > 0 or len(results[j+n_motifs]) > 0:
                adata.varm['motif_match'][i, j] = 1

    return None

