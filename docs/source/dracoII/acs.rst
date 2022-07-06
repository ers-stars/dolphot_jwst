HST/ACS
=====

.. _files:
.. _parameter:
.. _preprocessing:
.. _running:
.. _output:
.. _catalogs:
.. _asts:


For this example, we will produce run DOLPHOT on the HST/ACS F606W and F814W imaging of Draco II taken as part of program GO-14734.

Files
------------

We first set up a local directory structure that will house the flc and drc files downloaded from MAST and handle the main DOLPHOT operations. 

.. code-block:: bash
 
 > pwd
 > photometry/dracoii/acs/
 > ls
 > raw
 
In this case, DOLPHOT will operate on files in the 'acs' directory and downloaded images will be in the 'raw' subdirectory.

For this dataset, the contents of the raw subdirectory are

.. code-block:: bash
 
 > pwd
 > photometry/dracoii/acs/
 > ls raw/
 > jdan18010_drc.fits.gz  jdan18bsq_flc.fits.gz  jdan18c0q_flc.fits.gz  jdan19010_drc.fits.gz  jdan19xqq_flc.fits.gz  jdan19xxq_flc.fits.gz
   jdan18boq_flc.fits.gz  jdan18byq_flc.fits.gz  jdan18c5q_flc.fits.gz  jdan19xoq_flc.fits.gz  jdan19xvq_flc.fits.gz  jdan19y1q_flc.fits.gz
 

The next step is to copy the raw files up a level to the 'acs' directory.  Because DOLPHOT modifies the fits files, we want to preserve the original files in case we need to re-analyze them.

.. code-block:: bash
 
 > pwd
 > photometry/dracoii/acs/raw
 > cp *.flc.fits.gz ../
 > cp jdan18010_drc.fits.gz ../
 > cd ..
 > gunzip *.gz
 > ls *flc.fits
 > jdan18boq_f606w_flc.fits  jdan18byq_f606w_flc.fits  jdan18c5q_f606w_flc.fits  jdan19xqq_f814w_flc.fits	jdan19xxq_f814w_flc.fits
   jdan18bsq_f606w_flc.fits  jdan18c0q_f606w_flc.fits  jdan19xoq_f814w_flc.fits  jdan19xvq_f814w_flc.fits	jdan19y1q_f814w_flc.fits
 > ls *drc.fits
 > jdan18010_f606w_drc.fits
 
 .. note::
 DW: In this case, a python script also renamed the files to add the filter name.  We'll have to decide how to include little things (like this) in the documentation.

Preprocessing
------------

acsmask
^^^^^^^^^^^^



Parameter File
------------

Running DOLPHOT
------------

Examining Output
------------

Creating Stellar Catalogs
------------

Artificial Star Tests
------------
