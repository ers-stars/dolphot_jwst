File Stucture
=========


We first set up a local directory structure that will house the images downloaded from MAST and handle the main DOLPHOT operations. A recommended structure is to have a directory dedicated to DOLPHOT operations and a directory that contains the raw images. For example, if we were working with a subset of the M92 NIRCam data, we would have the following file structure

.. code-block:: bash
 
 > pwd
 > photometry/m92/nircam
 > ls
 > raw
 
In this case, DOLPHOT will operate on files in the 'nircam' directory and images downloaded from MAST will be in the 'raw' subdirectory.

For this dataset, the contents of the raw subdirectory are

.. code-block:: bash
 
 > pwd
 > photometry/m92/nircam/
 > ls raw/
 >jw01334-o001_t001_nircam_clear-f090w_i2d.fits
 >jw01334-o001_t001_nircam_clear-f150w_i2d.fits
 >jw01334001001_02101_00001_nrca1_o001_cal.fits
 >jw01334001001_02101_00001_nrca2_o001_cal.fits
 >jw01334001001_02101_00001_nrca3_o001_cal.fits
 >jw01334001001_02101_00001_nrca4_o001_cal.fits
 >jw01334001001_02101_00002_nrca1_o001_cal.fits
 >jw01334001001_02101_00002_nrca2_o001_cal.fits
 >jw01334001001_02101_00002_nrca3_o001_cal.fits
 >jw01334001001_02101_00002_nrca4_o001_cal.fits
 >jw01334001001_04101_00001_nrca1_o001_cal.fits
 >jw01334001001_04101_00001_nrca2_o001_cal.fits
 >jw01334001001_04101_00001_nrca3_o001_cal.fits
 >jw01334001001_04101_00001_nrca4_o001_cal.fits
 >jw01334001001_04101_00002_nrca1_o001_cal.fits
 >jw01334001001_04101_00002_nrca2_o001_cal.fits
 >jw01334001001_04101_00002_nrca3_o001_cal.fits
 >jw01334001001_04101_00002_nrca4_o001_cal.fits



 

Because DOLPHOT modifies the image files, we want to preserve the original files in case we need to re-analyze them.  So we copy images from the raw directory into the main directory.

.. code-block:: bash
 
 > pwd
 > photometry/m92/nircam/raw
 > cp *cal.fits ../
 > cp *i2d.fits ../
 > cd ../
 > ls *cal.fits
 >jw01334001001_02101_00001_nrca1_o001_cal.fits
 >jw01334001001_02101_00001_nrca2_o001_cal.fits
 >jw01334001001_02101_00001_nrca3_o001_cal.fits
 >jw01334001001_02101_00001_nrca4_o001_cal.fits
 >jw01334001001_02101_00002_nrca1_o001_cal.fits
 >jw01334001001_02101_00002_nrca2_o001_cal.fits
 >jw01334001001_02101_00002_nrca3_o001_cal.fits
 >jw01334001001_02101_00002_nrca4_o001_cal.fits
 >jw01334001001_04101_00001_nrca1_o001_cal.fits
 >jw01334001001_04101_00001_nrca2_o001_cal.fits
 >jw01334001001_04101_00001_nrca3_o001_cal.fits
 >jw01334001001_04101_00001_nrca4_o001_cal.fits
 >jw01334001001_04101_00002_nrca1_o001_cal.fits
 >jw01334001001_04101_00002_nrca2_o001_cal.fits
 >jw01334001001_04101_00002_nrca3_o001_cal.fits
 >jw01334001001_04101_00002_nrca4_o001_cal.fits
 > ls *i2d.fits
 >jw01334-o001_t001_nircam_clear-f090w_i2d.fits
 >jw01334-o001_t001_nircam_clear-f150w_i2d.fits
 
.. note::
 DOLPHOT works best when used on non-drizzled images (i.e., CAL or CRF files in the case of JWST, FLT or FLC in the case of HST). However, it is useful to include a deeper stacked image as a reference frame, to help image alignment and improve the overall photometry. In this example, we are going to use the stacked I2D image in the F150W band.
 
