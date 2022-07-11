File Stucture
=========


We first set up a local directory structure that will house the images downloaded from MAST and handle the main DOLPHOT operations. A recommended structure is to have a directory dedicated to DOLPHOT operations and a directory that contains the raw images.  For example, if we were working with M92 NIRCam data, we would have the following file structure

.. code-block:: bash
 
 > pwd
 > photometry/m92/nircam
 > ls
 > raw
 
In this case, DOLPHOT will operate on files in the 'nircam' directory and downloaded images will be in the 'raw' subdirectory.
