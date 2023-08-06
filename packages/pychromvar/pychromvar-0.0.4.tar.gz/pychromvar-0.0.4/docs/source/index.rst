Welcome to pychromVAR's documentation!
==============================================================

pychromVAR is a python package for inferring transcription factor binding variability from 
scATAC-seq data by implmenting the algorithm proposed in 
`chromVAR <https://github.com/GreenleafLab/chromVAR>`__. 
It is built on `anndata <https://anndata.readthedocs.io/en/latest/>`__ and 
`mudata <https://mudata.readthedocs.io/en/latest/>`__ therefore can work seamlessly 
with `scanpy <https://scanpy.readthedocs.io/en/stable/>`__ and
`muon <https://muon.readthedocs.io/en/latest/>`__ pipeline.

For more methdological detials, please refer to the original `paper <https://www.nature.com/articles/nmeth.4401>`__.

Installation
============

**pychromVAR** requires Python version >= 3.8 to run.

PyPI
----
**pychromVAR** is also available on PyPI:

.. code-block:: console

   pip install pychromvar

.. toctree::
   :caption: pychromvar
   :maxdepth: 1
   :hidden:
   
   api

.. toctree::
   :caption: notebooks
   :maxdepth: 1
   :hidden:

   notebooks/run_chromVAR
   notebooks/compare_with_chromVAR
   notebooks/multimodal_pbmc_3k

   