.. _Parameter Definitions:

Parameter Definitions
=========

Default values are indicated for most parameters.  Note the difference between interger (1) and decimal values (1.0).  Values for camera-specific paraemters depend on the instrument used.

Files
----------

* **Nimg** = 1: The number of images to be photometered.  The reference image should not be included in this number.
* **img_file**:  The base filename of the image (i.e., base filename minus '.fits').  img0_file is the reference image. img1_file to imgN_file are the images to be photometered.

Alignment 
---------

* **Align** = 1: Align images to reference? Allowed values are 0 (no), 1 (x/y offsets only), 2 (x/y offsets plus scale difference), 3 (x/y offsets plus distortion), and 4 (full third-order polynomial fit).
* **UseWCS** = 0: Use WCS header information for alignment? Allowed values are 0 (no), 1 (use to estimate shift, scale, and rotation), or 2 (use to estimate a full distortion solution). Note that any shifts or rotations selected by img shift and img xform are applied in addition to what is determined by the WCS solution. If reducing HST data, selecting UseWCS=1 can eliminate the need for running the fitdistort utilities. UseWCS=2 generally is not recommended for HST data since the distortion coefficients provided with DOLPHOT provide higher-order corrections than do the WCS headers.
* **aligntol** = 0: Tolerance on initial alignment solution. If greater than zero, DOLPHOT will search for matches out to the specified distance (in image pixels) from the initial guess. Must be a non-negative value.
* **Rotate** = 0: Correct for rotation in alignment? Allowed values are 0 (no) and 1 (yes).
* **img_shift** = 0 0: The offset of a science image relative to reference image. This value can be an initial guess that is later adjusted by DOLPHOT. Values are x and y on the image minus x and y on the reference image. Note that this parameter should not be set for the reference image.
* **img_xform** =1 0 0: The scale ratio, cubic distortion, and rotation of a science image relative to the reference image. This value can be an initial guess that is later adjusted by DOLPHOT. This parameter should not be set for the reference image, only for science images (i.e., img1_xform to imgN_xform).

.. note::
   * JWST requires UseWCS=2.  UseWCS=2 should also be set when running JWST and HST data together, even though it is not optimal for HST photometry alone.


Star Finding Parameters
----------

* **SecondPass** = 1: Number of additional passes when finding stars to locate stars in the wings of brighter stars. Must be a non-negative value.
* **RCentroid** = 1: The centroid used for obtaining initial positions of stars is a square of size 2RCentroid + 1 on each side.
* **SearchMode** = 1: Sets the minimization used to determine star positions. Allowed values are 0 (chi divided by SNR) and 1 (chi only). A value of one appears safe for all applications. A value of zero has been seen to fail if images of very different exposure times are used together.
* **SigFind** = 2.5: Sigma detection threshold. Stars above this limit will be kept in the photometry until the final output.
* **SigFindMult** = 0.85: Multiple for sigma detection threshold in initial finding algorithm. This should be close to one for larger PSFs, and as low as 0.75 for badly undersampled PSFs.
* **SigFinal** = 3.5: Sigma threshold for a star to be listed in the final photometry list. To get all stars, set SigFinal equal to SigFind.
* **PosStep** = 0.25: Typical stepsize in x and y during photometry iterations. Should be set to a factor of a few smaller than the PSF FHWM.
* **dPosMax** = 3.0: Maximum position change of a star during a single photometry itera- tion. Note that this parameter is currently ignored.
* **RCombine** = 2.0: Minimum separation of two stars (they will be combined if they become closer than this value). This value can generally be about 2/3 of the PSF FWHM, but setting below 1.4 will not always be effective.
* **FSat** = 0.999: Fraction of nominal saturation for which pixels are considered saturated.

Photometry
---------

* **PSFPhot** = 1: Type of photometry to be run. Options are 0 (aperture), 1 (standard PSF-fit), 2 (PSF-fit weighted for central pixels). Option 1 is suggested for most photometric needs, but option 0 can provide superior photometry if the signal-to- noise is high and the field is uncrowded.
* **PSFPhotIT** = 2: Number of iterations on the PSF photometry solution, if PSFPhot is 1 or 2. This will refine the noise estimates on the pixels based on the model fit.
* **FitSky** = 1: Sky-fitting setting. Options are 0 (use the sky map from calcsky), 1 (fit the sky normally prior to each photometry measurement), 2 (fit the sky inside the PSF region but outside the photometry aperture), 3 (fit the sky within the photometry aperture as a 2-parameter PSF fit), and 4 (fit the sky within the photometry aperture as a 4-parameter PSF fit). Options 1 and 3 are the suggested settings. Option 0 should be used only if the field is very uncrowded; option 2 can be used in extremely crowded fields; option 4 can help in fields with strong background gradients. FitSky=4 is unstable and not recommended except in extreme gradients.
* **SkipSky** = 1: Sampling of sky annulus; set to a number higher than 1 to gain speed at the expense of precision. This is only used if FitSky is set to 1. In general, this should never be larger than the FWHM of the PSF.
* **SkySig** = 2.25: Sigma rejection threshold for sky fit; only used if FitSky is set to 1.
* **MaxIT** = 25: Maximum number of photometry iterations.
* **NoiseMult** = 0.05: To allow for imperfect PSFs, the noise is increased by this value times the star brightness in the pixel when computing chi values.
* **SigPSF** = 10.0: Minimum signal-to-noise for a PSF solution to be attempted on a star. Fainter detections are assigned type 2.
* **CombineChi** = 0: CombineChi affects the combined photometry blocks. If set to zero, photometry will be combined weighted by 1/σ2 to maximize signal to noise. If set to one, weights will be 1/σ2max(1, χ2) to reduce the impact of epochs with bad photometry. Note that using CombineChi of one will require tuning NoiseMult so that well measured stars have χ = 1 at all magnitudes (plots of chi vs. magnitude should show this). Note also that this will result in larger uncertainties for combined (but not individual image) magnitudes and normalized count rates, as the individual image uncertainties are effectively multiplied by χ when calculating combined magnitudes.

.. note::
   * In general, FitSky=2 provides the most robust results across a wide range of crowding.


Camera Specific
-----------

* **img_rsky** *(int int)*: Inner and outer radii for computing sky values, if FitSky=1 is being used. Also used in a few places if using FitSky = 2, 3, or 4, so should always be set. The inner radius (first number) should be outside the bulk of the light from the star; the outer (second) should be sufficiently large to compute an accurate sky.
* **img_rsky2** *(int int)**: The annulus setting when using FitSky=2.
* **img_RSF**: The size of the PSF used for star subtraction, as well as the size of the PSF residual calculated if PSFRes is set to 1
* **img_apsky** *(int int)*: Set the inner and outer radii of the annulus used for calculating sky values for aperture corrections.

Other
---------

* **DiagPlotType**: Generate diagnostic plots showing aperture corrections, PSF correction image, and alignment residuals. Options are PS, GIF, and PNG. Plots are generated only if PGPLOT is used.
* **VerboseData** = 0: Generates a file named “.data” that includes all numbers output to the console while running (alignment, PSF solution, aperture corrections).  Turned off (set to 0) by default.
* **xytfile**: Used for the DOLPHOT warmstart option in which you can predetermine a list of stars to be photometered. The format of the warmstart file is the extension, Z, X, Y, type, and signal-to-noise of each star. The extension, Z, and type must be provided in regular integer format - no decimals are allowed. To run in this mode the warmstart file should be specified with the xytfile option set to the star list filename.
* **psfstars**: Specify coordinates of the PSF stars. The file must contain extension, chip, X, and Y (the first four columns of DOLPHOT output).
* **ApCor** = 1: Make aperture corrections? Allowed values are 0 (no) and 1 (yes). Default aperture corrections always have the potential for error, so it is strongly recom- mended that you manually examine the raw output from this process.
* **Force1** = 0: Force all objects to be of class 1 or 2 (i.e., stars)? Allowed values are 0 (no) and 1 (yes). For crowded stellar fields, this should be set to 1 and the χ and sharpness values used to discard extended objects.
* **FlagMask** = 4*(HST modules)*: FlagMask is a bitwise mask that determines what error flags will not be accepted when producing the combined photometry blocks for each filter. Note that error flag values of eight or more (when the “extreme case”) always cause the photometry to be ignored. A value of zero allows photometry with an error flag less than eight to be used. Adding one eliminates stars close to the chip edge, adding two eliminates stars with too many bad pixels, and adding four eliminates stars with saturated cores.
* **InterpPSFlib** = 1: Spatially interpolate the PSF (0/1 no/yes). If InterpPSFlib is set to 0, the PSF library will use the nearest X,Y position where a precalculated PSF is available rather than interpolating. The impact is ~1% on the PSF shape but some speed improvement.
* **PSFres** = 1: Solve for PSF residual image? Allowed values are 0 (no) and 1 (yes). Turning this feature off can create nonlinearities in the photometry unless PSFphot is also set to zero.

