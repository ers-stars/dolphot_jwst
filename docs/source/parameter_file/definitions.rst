Parameter Definitions
=========

Files
----------

* **Nimg**: The number of images to be photometered.  The reference image should not be included in this number.
* **img_file**:  The base filename of the image (i.e., base filename minus '.fits').  img0_file is the reference image. img1_file to imgN_file are the images to be photometered.

Alignment
---------

* **Align**:
* **UseWCS**:
* **aligntol**:
* **Rotate**:
* **img_shift** *(int int)*: The offset of a science image relative to reference image. This value can be an initial guess that is later adjusted by DOLPHOT. Values are x and y on the image minus x and y on the reference image. Note that this parameter should not be set for the reference image.
* **img_xform** *(int int int)*: The scale ratio, cubic distortion, and rotation of a science image relative to the reference image. This value can be an initial guess that is later adjusted by DOLPHOT. This parameter should not be set for the reference image, only for science images (i.e., img1_xform to imgN_xform).


Star Finding Parameters
----------

* **SecondPass**:
* **RCentroid**:
* **SearchMode**:
* **SigFind**:
* **SigFindMult**:
* **SigFinal**:
* **PosStep**:
* **dPosMax**:
* **RCombine**:
* **FSat**:

Photometry
---------

* **PSFPhot**:
* **SkipSky**:
* **SkySig**:
* **MaxIT**:
* **NoiseMult**:
* **SigPSF**:
* **CombineChi**:

Camera Specific
-----------

* **img_rsky**:
* **img_psf**:
* **img_apsky**:
* **ACSuseCTE**:
* **WFC3useCTE**:
* **ACSpsfType**:
* **WFC3IRpsfType**:
* **WFC3UVIESpsfType**:

Other
---------

* **DiagPlotType**:
* **xytfile**:
* **xytpsf**:
* **psfstars**:
* **ApCor**:
* **Force1**:
* **FlagMask**: 
* **InterpPSFlib**:
* **PSFres**:
* **psfoff**:

