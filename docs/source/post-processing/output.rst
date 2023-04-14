Examining the output
============
When *dolphot* has completed running, we need to make sure the reduction run is successful and the photometry reliable. This is done through inspection of the many diagnostic files produced during reduction, as well as inspection of the output photometric catalog.

The first file we wish to examine is the log file where we captured *dolphot* standard output. This log contains useful information on about the many steps of the reduction. The first step is to make sure the images were read in correctly and the CCD parameters were set to reasonable values. In the case of our M92 example, our log reports:

.. code-block:: bash

  Reading IMAGE extension: 2048x2048
    GAIN=2.08 EXP=311s NOISE=11.43 BAD=-740.28 SAT=335568.78
  Reading IMAGE extension: 2048x2048
    GAIN=2.02 EXP=311s NOISE=10.52 BAD=-334.05 SAT=423324.06
  Reading IMAGE extension: 2048x2048
    GAIN=2.17 EXP=311s NOISE=10.34 BAD=-604.93 SAT=321757.56
  Reading IMAGE extension: 2048x2048
    GAIN=2.02 EXP=311s NOISE=10.60 BAD=-203.43 SAT=321226.41
  Reading IMAGE extension: 2048x2048
    GAIN=2.01 EXP=311s NOISE=11.77 BAD=-1369.48 SAT=327728.19
  Reading IMAGE extension: 2048x2048
    GAIN=2.14 EXP=311s NOISE=12.77 BAD=-451.42 SAT=387245.75
  Reading IMAGE extension: 2048x2048
   GAIN=1.94 EXP=311s NOISE=11.85 BAD=-253.31 SAT=397041.56
  ...
  
If anything did not proceed correctly with the pre-processing routines (e.g., *nircammask*) it will usually manifest in the image parameters. Make sure that **GAIN**, **BAD** and **SAT** are *reasonable* values (i.e., low unity, moderatley negative numbers, and large positive numbers, respectively). 

If the images are read in correctely, a common source of problems has to do with the astrometric alignment of the frames. DOLPHOT calculates geometric transformations between each of the science frames and the reference image. If the transformations are not sufficiently accurate, the photometry will typically suboptimal. In our M92 example, we can check the aligment in the log file:

.. code-block:: bash

  38234 stars for alignment
  image 1: 1829 matched, 1781 used, 0.15 -0.02 1.000000 0.00000 -0.004, sig=0.10
  image 2: 2043 matched, 1971 used, 0.18 -0.12 1.000000 0.00000 0.003, sig=0.12
  image 3: 4142 matched, 3964 used, 0.06 0.00 1.000000 0.00000 0.000, sig=0.12
  image 4: 4885 matched, 4661 used, 0.07 -0.13 1.000000 0.00000 -0.004, sig=0.13
  image 5: 1436 matched, 1404 used, 0.13 -0.01 1.000000 0.00000 -0.004, sig=0.13
  image 6: 1506 matched, 1458 used, 0.15 -0.10 1.000000 0.00000 0.003, sig=0.11
  
The two key metrics to monitor here are the number of matched stars for each image, and the **sig** values, which is the rms residual in *px* around the adopted trasnformation. The acceptable values for matched stars and **sig** depend somewhat on how dense the stellar field is and what camera is being analyzed. For a moderately populated NIRCam field, we want most of the images to have at least 100 matched stars and **sig** values below 0.30. 





When *dolphot* is run with the following syntax:

.. code-block:: bash

  > dolphot <outputname> <options> > <logfile>
  
the output photometric catalog is stored in the **outputname** file. This file contains a output line for each point-source identified during the reduction run. For each line, the **outputname** file contains a long list of outputs. These include photometric measurements and quality flags on each indivual frame, as well as combined photometry from multiple images that use the same filter.
