Setup
========

Once the images have been preprocessed, we are ready to run the PSF-photometry routine. This is invoked with the *dolphot* command, which has the following syntax:

.. code-block:: bash

  > dolphot <outputname> <options>
  
The **outputname** file is where the photometric catalog will be stored. A number of auxiliary files, using **outputname** as root, will also be created to store additional information and diagnostics. The **options** keywords set the value of a number of parameters used during the PSF-photometry . This includes the name of each image that needs to be photometered (**img_<1-N>**), and which image has to be used as reference frame (**img_0**). A list of major dolphot parameters is provided in :ref:`Parameter Definitions`. The parameter values can be set from the command line:

.. code-block:: bash

  > dolphot <outputname> <parametername>=<parametervalue>
  
Any omitted parameter will be set at the default value (see :ref:`Parameter Definitions`). If we want to specify a large number of parameters, we can store them in a parameter file:

.. code-block:: bash

  > dolphot <outputname> -p<parameterfile>
  
While running, *dolphot* will print diagnostics on the reduction on the standard output. Since these are useful to assess the outcome of the reduction and troubleshoot problems, we may wish to save them in a log file. 

Continuing with our example dataset, we will run the reduction on our M92 images:

.. code-block:: bash

  > dolphot M92_example.phot -pphot.param > phot.log
  
In this example, **phot.param** file contains the following input:

.. code-block:: bash

 Nimg = 60
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
 ...
 img48_file = jw01334001001_04101_00004_nrcb4_cal
 img49_file = jw01334001001_02101_00001_nrcalong_cal
 img50_file = jw01334001001_02101_00001_nrcblong_cal
 img51_file = jw01334001001_02101_00002_nrcalong_cal
 img52_file = jw01334001001_02101_00002_nrcblong_cal
 ...

 img1_raper = 2
 img1_rchi = 1.5
 img1_rsky2 = 3 10
 img2_raper = 2
 img2_rchi = 1.5
 img2_rsky2 = 3 10
 ...
 img49_raper = 3
 img49_rhi = 2.0
 img49_rsky2 = 4 10
 ...

 rsky0 = 15
 rsky1 = 35
 rpsf = 15
 apsky = 20 35
 FitSky = 2
 SigPSF = 5.0
 FlagMask = 4
 SecondPass = 5
 PSFPhotIt = 2
 ApCor = 1
 FSat = 0.999
 NoiseMult = 0.1
 RCombine = 1.5
 CombineChi = 0
 MaxIT = 25
 InterpPSFlib = 1
 SigFindMult = 0.85
 PSFPhot = 1
 Force1 = 0
 SkySig = 2.25
 SkipSky = 1
 UseWCS = 2
 PSFres = 1
 PosStep = 0.25


.. note::
  Because we are working with images from both the short-wavelength and long-wavelength channels, we need to speficy specific values of **raper**, **rchi**, and **rsky2** for each image, as the recommended value changes between the two sets of images (see `Weisz et al. 2024 
  <https://DUD>`_). If working with a homogeneous set of images (e.g., only from the short-wavelength channel), the parameter value can be set just once. This is done by replacing the list of **img<1-N>_<parametername>** with a single **<parametername>** instance. 
  
  
