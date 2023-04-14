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








When *dolphot* is run with the following syntax:

.. code-block:: bash

  > dolphot <outputname> <options> > <logfile>
  
the output photometric catalog is stored in the **outputname** file. This file contains a output line for each point-source identified during the reduction run. For each line, the **outputname** file contains a long list of outputs. These include photometric measurements and quality flags on each indivual frame, as well as combined photometry from multiple images that use the same filter.
