Setup
========

Once the images have been preprocessed, we are ready to run the PSF-photometry routine. This is invoked with the *dolphot* command, which has the following sintax:

.. code-block:: bash

  > dolphot <outputname> <options>
  
The **outputname** file is where the photometric catalog will be stored. A number of auxiliary files, using **outputname** as root, will also be created to store additional information and diagnostics. The **options** keywords set the value of a number of parameters used during the PSF-photometry . This includes the name of each image that needs to be photometered (**img_<1-N>**), and which image has to be used as reference frame (**img_0**). A list of major dolphot parameters is provided in `Parameter Definitions`_. The parameter values can be set from the command line:

.. code-block:: bash

  > dolphot <outputname> <parametername>=<parametervalue>
  
Any omitted parameter will be set at the default value (cf. `Parameter Definitions`_). If we want to specify a large number of parameters, we can store them in a parameter file:

.. code-block:: bash

  > dolphot <outputname> -p<parameterfile>
  
While running, *dolphot* will print diagnostics on the reduction on the standard output. Since these are useful to assess the outcome of the reduction and troubleshoot problems, we may wish to save them in a log file. 

Continuing with our example dataset, we will run the reduction on our M92 images:

.. code-block:: bash

  > dolphot M92_example.phot -pphot.param > phot.log
  
In this example, **phot.param** file contains the following input:

.. code-block:: bash

  Nimg = 16
  img0_file = jw01334-o001_t001_nircam_clear-f150w_i2d
  img1_file = jw01334001001_02101_00001_nrca1_cal
  img2_file = jw01334001001_02101_00001_nrca2_cal
  img3_file = jw01334001001_02101_00001_nrca3_cal
  img4_file = jw01334001001_02101_00001_nrca4_cal
  img5_file = jw01334001001_02101_00001_nrcb1_cal
  img6_file = jw01334001001_02101_00001_nrcb2_cal
  img7_file = jw01334001001_02101_00001_nrcb3_cal
  img8_file = jw01334001001_02101_00001_nrcb4_cal
  img9_file = jw01334001001_02101_00002_nrca1_cal
  img10_file = jw01334001001_02101_00002_nrca2_cal
  img11_file = jw01334001001_02101_00002_nrca3_cal
  img12_file = jw01334001001_02101_00002_nrca4_cal
  img13_file = jw01334001001_02101_00002_nrcb1_cal
  img14_file = jw01334001001_02101_00002_nrcb2_cal
  img15_file = jw01334001001_02101_00002_nrcb3_cal
  img16_file = jw01334001001_02101_00002_nrcb4_cal

  raper = 2
  rchi = 1.5
  rsky0 = 15
  rsky1 = 35
  rsky2 = 3 10
  rpsf = 15
  apsky = 20 35
  FitSky = 2
  SigPSF = 5.0
  FlagMask = 4
  SecondPass = 5
  PSFPhotIt = 2
  NoiseMult = 0.1
  RCombine = 1.5
  CombineChi = 0
  InterpPSFlib = 1
  UseWCS = 2


  
  
