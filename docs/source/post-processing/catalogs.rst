Culling the catalog
=============

We now have completed a successful DOLPHOT reduction and built our photometric catalog. However, practical applications require further post-processing to ensure we work with a meaningful source list. The catalog in **outputname**.phot, in fact, contains a fairly large number of contaminant sources, including background galaxies, artifacts, blends, poorly photometered stars, etc. This is obvious by inspecting the color-magnitude diagram.


In order to reduce these contaminants and obtain a catalog that contains mostly bona-fide stars, it is useful to inspect the quality parameters that DOLPHOT has calculated for each source. These parameters are listed both for the global photometry and for each individual filter, and include:

* **Type** (only given for global photometry): If **Force1** has been set to 0, this can be 1 (bright star, as set by **sigPSF**), 2 (faint star), 3 (elongated source), 4 (object too narrow), or 5 (extended source). If **Force1** has been set to 1, this parameter can only be 1 or 2. 
* **Chi**: The Chi-squared from the PSF-fit
* **SNR**: The signal-to-noise ratio of the source
* **Sharpness**: The angular extent of the source, compared to the PSF FWHM. A perfect point source would have a Sharpness of 0. A large positive Sharpness means that the source is extended (e.g., a background galaxy). A large negative Sharpness means that the source is narrower than the PSF (e.g., a hot pixel).
* **Roundness**: The ellipticity of the source's light-profile. A perfectly circular source has a Roundness value of 0.
* **Crowding**: The amount of contamination from neighboring sources. The value of Crowding is in magnitudes and represents how much brighter the star would have been measured had nearby stars not been fit simultaneously.
* **Quality Flag** (only given per filter): 0 if the source was fit without issues. A value of 1 is added if the photometry aperture extends off chip. A value of 2 is added is there are too many bad or saturated pixels. A value of 4 is added is the source is saturated at the center. A value of 8 is added for extreme cases of these problems. Multiple values can be added to flag.



