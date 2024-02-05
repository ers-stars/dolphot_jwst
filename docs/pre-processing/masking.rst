Applying image masks
===========
Before running the DOLPHOT photometric pipeline, the images need to be pre-processed to be suitable for PSF-fitting photometry.
This is accomplished through the mask routines *nircammask* and *nirissmask*. Specifically, these routines will:

* Mask out bad or saturated pixels using the Data Quality (DQ) array included in the images.
* Convert units from MJy/sr to DN. This is done by diving the pixel values by the FITS keyword PHOTMJSR and multiplying them by the exposure time (see Note).
* For distorted images (non-drizzled) multiply the pixel value by the pixel area map.
* Add the readout noise and gain values in the FITS header.

Continuing our M92 example, we are going to execute *nircammask* on the reference image:

.. code-block:: bash

  > nircammask -etctime jw01334-o001_t001_nircam_clear-f150w_i2d.fits
  
And on each of the CAL files:

.. code-block:: bash

  > nircammask -etctime jw01334001001_02101_00001_nrca1_o001_cal.fits
  > nircammask -etctime jw01334001001_02101_00001_nrca2_o001_cal.fits
  > nircammask -etctime jw01334001001_02101_00001_nrca3_o001_cal.fits
  ...

.. note::
  * While the mask routines are ultimately intended to use the DQ array for pixel flagging, as of writing, *nircammask* and *nirissmask* use a different strategy, to compensate for current JWST DQ limitations. In particular bad pixels in CAL and CRF images are identified by having a SCI array value of exactly 0, while saturated pixels are identified by having a DQ flag of 2. Bad pixels on the I2D images are identified by having a WHT array value of exactly 0. The mask utilities have been updated to accept NaN as a secondary signal for a bad pixel.
  * For JWST cameras, the exposure time needed in the mask routine is the *Time Between First and Last Measurement*, which can differ from both the EFFEXPTM and DURATION FITS keywords. Use of the *-etctime* flag ensures that the exposure time is accurately calculated. Executing the mask routine without the *-etctime* flag will use the EFFEXPTM FITS keyword instead. This only applies to JWST images and it is not relevant to HST datasets.
  * Similar routines (e.g., *acsmask*, *wfc3mask*) exist within the HST modules of DOLPHOT. Usage is similar to *nircammask* and *nirissmak*. However, for HST cameras that contain multiple chips, such as ACS/WFC, and additional step is required after masking. This step is needed to save individual chip images into separate .fits files, and it is achieved using the *splitgroups* routine. 
  * The *splitgroups* step is not required if only JWST images are being run with DOLPHOT, as the STScI pipeline creates individual .fits files for each of the detector chips. However, if JWST and HST images are being run through DOLPHOT together, then *splitrgoups* needs to be run on all images (JWST and HST) to ensure consistent file formats for DOLPHOT.
