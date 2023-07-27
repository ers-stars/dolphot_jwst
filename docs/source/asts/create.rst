Creating Artifical Star Lists
============

A useful capability of DOLPHOT is to perform artifical star tests (ASTs) to evaluate photometric errors, systematic uncertainties and completenss across the CMD. To do so, DOLPHOT injects mock stellar sources in the images, with realistic noise properties, and performs photometry on them using the same set up used for reduction. The first step to perform ASTs is to create a suitable list of input mock stars, that will be injected in the dataset. The input list will consist of multiple entries, one per star, having the following format:

.. code-block:: bash

  1 1 X Y M1 M2 M3...
  1 1 X Y M1 M2 M3...
  1 1 X Y M1 M2 M3...
  ...

Where the first two numbers are the extension number and chip number in the image (both 1, for a typical JWST reduction); X and Y are the pixel coordinate of the mock star, in the coordinate system of the reference image; and the following numbers are the input magnitudes in each of the photometered filters.

.. note::

  The extension number will need to be set to 0, if the frames have been processed through *splitgroups*. This is the case, for instance, is the images are reduced together with HST frames.

