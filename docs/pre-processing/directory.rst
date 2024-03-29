File structure
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
 >jw01334001001_02101_00001_nrca1_cal.fits
 >jw01334001001_02101_00001_nrca2_cal.fits
 >jw01334001001_02101_00001_nrca3_cal.fits
 >jw01334001001_02101_00001_nrca4_cal.fits
 >jw01334001001_02101_00001_nrcalong_cal.fits
 >jw01334001001_02101_00001_nrcb1_cal.fits
 >jw01334001001_02101_00001_nrcb2_cal.fits
 >jw01334001001_02101_00001_nrcb3_cal.fits
 >jw01334001001_02101_00001_nrcb4_cal.fits
 >jw01334001001_02101_00001_nrcblong_cal.fits
 >jw01334001001_02101_00002_nrca1_cal.fits
 >jw01334001001_02101_00002_nrca2_cal.fits
 >jw01334001001_02101_00002_nrca3_cal.fits
 >jw01334001001_02101_00002_nrca4_cal.fits
 >jw01334001001_02101_00002_nrcalong_cal.fits
 >jw01334001001_02101_00002_nrcb1_cal.fits
 >jw01334001001_02101_00002_nrcb2_cal.fits
 >jw01334001001_02101_00002_nrcb3_cal.fits
 >jw01334001001_02101_00002_nrcb4_cal.fits
 >jw01334001001_02101_00002_nrcblong_cal.fits
 >jw01334001001_02101_00004_nrca1_cal.fits
 >jw01334001001_02101_00004_nrca2_cal.fits
 >jw01334001001_02101_00004_nrca3_cal.fits
 >jw01334001001_02101_00004_nrca4_cal.fits
 >jw01334001001_02101_00004_nrcalong_cal.fits
 >jw01334001001_02101_00004_nrcb1_cal.fits
 >jw01334001001_02101_00004_nrcb2_cal.fits
 ...




 

Because DOLPHOT modifies the image files, we want to preserve the original files in case we need to re-analyze them.  So we copy images from the raw directory into the main directory.

.. code-block:: bash
 
 > pwd
 > photometry/m92/nircam
 > cp raw/*cal.fits .
 > cp raw/*i2d.fits .
 > ls *i2d.fits
 >jw01334-o001_t001_nircam_clear-f090w_i2d.fits
 >jw01334-o001_t001_nircam_clear-f150w_i2d.fits
 > ls *cal.fits
 >jw01334001001_02101_00001_nrca1_cal.fits
 >jw01334001001_02101_00001_nrca2_cal.fits
 >jw01334001001_02101_00001_nrca3_cal.fits
 >jw01334001001_02101_00001_nrca4_cal.fits
 >jw01334001001_02101_00001_nrcalong_cal.fits
 >jw01334001001_02101_00001_nrcb1_cal.fits
 >jw01334001001_02101_00001_nrcb2_cal.fits
 >jw01334001001_02101_00001_nrcb3_cal.fits
 >jw01334001001_02101_00001_nrcb4_cal.fits
 >jw01334001001_02101_00001_nrcblong_cal.fits
 >jw01334001001_02101_00002_nrca1_cal.fits
 >jw01334001001_02101_00002_nrca2_cal.fits
 >jw01334001001_02101_00002_nrca3_cal.fits
 >jw01334001001_02101_00002_nrca4_cal.fits
 >jw01334001001_02101_00002_nrcalong_cal.fits
 >jw01334001001_02101_00002_nrcb1_cal.fits
 >jw01334001001_02101_00002_nrcb2_cal.fits
 >jw01334001001_02101_00002_nrcb3_cal.fits
 >jw01334001001_02101_00002_nrcb4_cal.fits
 >jw01334001001_02101_00002_nrcblong_cal.fits
 >jw01334001001_02101_00004_nrca1_cal.fits
 >jw01334001001_02101_00004_nrca2_cal.fits
 >jw01334001001_02101_00004_nrca3_cal.fits
 >jw01334001001_02101_00004_nrca4_cal.fits
 >jw01334001001_02101_00004_nrcalong_cal.fits
 >jw01334001001_02101_00004_nrcb1_cal.fits
 >jw01334001001_02101_00004_nrcb2_cal.fits
 ...
 
 
.. note::
 DOLPHOT is designed to only work on non-drizzled images (i.e., CAL or CRF files in the case of JWST, FLT or FLC in the case of HST). However, it is useful to include a deeper stacked image as a reference frame to help image alignment and improve the overall photometry. In this example, we are going to use the stacked I2D image in the F150W band.  
We strongly recommend using CAL files for photometry. We have found cases in which the CRF files simply do not work for photometry.
 
