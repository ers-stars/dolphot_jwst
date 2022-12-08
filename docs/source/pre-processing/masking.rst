Applying Image Masks
===========
Before running the DOLPHOT photometric pipeline, the images need to be pre-processed to be suitable for PSF-fitting photometry.
This is accomplished through the mask routines *nircammask* and *nirissmask*. Specifically, these routines will:

* Mask out bad or saturated pixels using the Data Quality (DQ) array included in the images.
* Convert units from MJy/sr to DN. This is done by diving the pixel values by the FITS keyword PHOTMJSR and multiplying them by the FITS keyword (EFFEXPTM)
* For distorted images (non-drizzled) multiply the pixel value by the pixel area map.
* Add the readout noise and gain values in the FITS header.

.. note::
  * While the mask routines are ultimately intended to use the DQ array for pixel flagging, as of writing, *nircammask* and *nirissmask* use a different strategy, to compensate for current DQ limitations. In particular bad pixels in CAL and CRF images are identified by having a SCI array value of exactly zero, while saturated pixels are identified by having a DQ flag of two. Bad pixels on the I2D images are identified by having a WHT array value of exactly zero.
  * Similar routines (e.g., *acsmask*, *wfc3mask*) exist within the HST modules of DOLPHOT. Usage a
NIRCam
------


NIRISS
------
