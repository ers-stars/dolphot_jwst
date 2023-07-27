Culling the catalog
=============

We now have completed a successful DOLPHOT reduction and built our photometric catalog. However, practical applications require further post-processing to ensure we work with a meaningful source list. The catalog in **outputname**.phot, in fact, contains a fairly large number of contaminant sources, including background galaxies, artifacts, blends, poorly photometered stars, etc. This is obvious by inspecting the color-magnitude diagram.


In order to reduce these contaminants and obtain a catalog that contains mostly bona-fide stars, it is useful to inspect the quality flags that DOLPHOT has calculated for each source. For each filter in the datset these include:

* **Chi**: The Chi-squared from the PSF-fit
* **SNR**: The signal-to-noise ratio of the source
* **Sharpness**: The angular extent of the source, compared to the PSF FWHM. A perfect point source would have a Sharpness of 0. A large positive Sharpness means that the source is extended (e.g., a background galaxy). A large negative Sharpness means that the source is narrower than the PSF (e.g., a hot pixel).
* **Roundness**:
* **Crowding**:
* **Quality Flag**:
