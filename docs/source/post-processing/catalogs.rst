Culling the catalog
=============

We now have completed a successful DOLPHOT reduction and built our photometric catalog. However, practical applications require further post-processing to ensure we work with a meaningful source list. The catalog in **outputname**.phot, in fact, contains a fairly large number of contaminant sources, including background galaxies, artifacts, blends, poorly photometered stars, etc. This is obvious by inspecting the color-magnitude diagram.


In order to reduce these contaminants and obtain a catalog that contains mostly bona-fide stars, it is useful to inspect the quality flags that DOLPHOT has calculated for each source. For each filter in the datset these include:
