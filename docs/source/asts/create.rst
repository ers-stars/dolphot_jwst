Creating Artifical Star Lists
============

A useful capability of DOLPHOT is to perform artifical star tests (ASTs) to evaluate photometric errors, systematic uncertainties and completenss across the CMD. To do so, DOLPHOT injects mock stellar sources in the images, with realistic noise properties, and performs photometry on them using the same set up used for reduction. The first step to perform ASTs is to create a suitable list of input mock stars, that will be injected in the dataset. The input list will consist of multiple entries having the following format:

.. code-block: bash
  1 1 X Y M1 M2 M3...


