File Stucture
=========


We first set up a local directory structure that will house the images downloaded from MAST and handle the main DOLPHOT operations. A recommended structure is to have a directory dedicated to DOLPHOT operations and a directory that contains the raw images. For example, if we were working with M92 NIRCam data, we would have the following file structure

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
 >
 

Because DOLPHOT modifies the image files, we want to preserve the original files in case we need to re-analyze them.  So we copy images from the raw directory into the main directory.

.. code-block:: bash
 
 > pwd
 > photometry/m92/nircam/raw
 > cp 
 > cp 
 > cd ..
 > gunzip *.gz
 > ls *flc.fits
 > 
 > ls *drc.fits
 > 
 
