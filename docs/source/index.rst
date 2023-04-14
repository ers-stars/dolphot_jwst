User's Guide for DOLPHOT NIRCAM and NIRISS modules
===================================

**DOLPHOT** is a widely used software package for resolved stellar photometry that is written and maintained by Andrew Dolphin.  General information about DOLPHOT can be found on its `homepage <http://americano.dolphinsim.com/dolphot/>`_.

This page contains information and examples for performing photometry with DOLPHOT on JWST NIRCam and NIRISS images acquired as part of the `JWST Early Release Science Program for Resolved Stellar Populations <https://ers-stars.github.io>`_ (DD-ERS-1334).

If you make use of DOLPHOT in your work please cite `Dolphin 2000 <https://ui.adsabs.harvard.edu/abs/2000PASP..112.1383D/abstract>`_ and `Dolphin 2016 <https://ui.adsabs.harvard.edu/abs/2016ascl.soft08013D/abstract>`_.  Our JWST survey design and first data reductions are described in `Weisz et al. 2023 <https://ui.adsabs.harvard.edu/abs/2023arXiv230104659W/abstract>`_.  A paper describing the NIRCam and NIRISS modules for DOLPHOT will be released in mid-2023 (*Weisz et al. in prep*).


.. note::

   DOLPHOT and this documentation are under active development.

.. toctree::
   :maxdepth: 1
   :Caption: Overview
   :name: overview

   overview/workflow
   overview/usage

.. toctree::
   :maxdepth: 1
   :caption: Installation
   :name: install

   install/install
   
.. toctree::
   :maxdepth: 3
   :caption: Pre-processing
   :name: preprocess
   
   pre-processing/directory
   pre-processing/masking
   pre-processing/sky
   
   
   
.. toctree::
   :maxdepth: 1
   :caption: Running DOLPHOT
   :name: param

   running_dolphot/setup
   running_dolphot/definitions
   
.. toctree::
   :maxdepth: 1
   :caption: Post-Processing
   :name: postprocess

   post-processing/output
   post-processing/catalogs
   
   
.. toctree::
   :maxdepth: 1
   :caption: Artificial Star Tests
   :name: asts

   asts/create
   asts/running
   asts/output
   
.. toctree::
   :maxdepth: 2
   :caption: Examples
   :name: examples
   
   examples/m92_niriss
 
