Applying Image Masks
===========
Before running the DOLPHOT photometric pipeline, the images need to be pre-processed to be suitable for PSF-fitting photometry.
This is accomplished through the mask routines *nircammask* and *nirissmask*. Specifically, these routines will:

* Mask out bad or saturated pixels using the Data Quality (DQ) array included in the images.
* Convert units from MJy/sr to DN. This is done by diving the pixel values by the FITS keyword PHOTMJSR and multiplying them by the FITS keyword EFFEXPTM.
* For distorted images (non-drizzled) multiply the pixel value by the pixel area map.
* Add the readout noise and gain values in the FITS header.

Continuing our M92 example, we are going to execute *nircammask* on the reference image:

.. code-block:: bash

  > nircammask jw01334-o001_t001_nircam_clear-f150w_i2d.fits
  
And on each of the CRF files:

.. code-block:: bash

  > nircammask jw01334001001_02101_00001_nrca1_o001_cal.fits
  > nircammask jw01334001001_02101_00001_nrca2_o001_cal.fits
  > nircammask jw01334001001_02101_00001_nrca3_o001_cal.fits
  ...

.. note::
  * While the mask routines are ultimately intended to use the DQ array for pixel flagging, as of writing, *nircammask* and *nirissmask* use a different strategy, to compensate for current JWST DQ limitations. In particular bad pixels in CAL and CRF images are identified by having a SCI array value of exactly zero, while saturated pixels are identified by having a DQ flag of two. Bad pixels on the I2D images are identified by having a WHT array value of exactly zero.
  * Similar routines (e.g., *acsmask*, *wfc3mask*) exist within the HST modules of DOLPHOT. Usage is similar to *nircammask* and *nirissmak*. However, for HST cameras that contain multiple chips, such as ACS/WFC, and additional step is required after masking. This step is needed to save individual chip images into separate .fits files, and it is achieved using the *splitgroups* routine. The *splitgroups* step is not required for JWST images, as the STScI pipeline creates individual .fits files for each of the detector chips.
