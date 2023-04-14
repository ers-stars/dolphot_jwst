Setup
========

Once the images have been preprocessed, we are ready to run the PSF-photometry routine. This is invoked with the *dolphot* command, which has the following sintax:

.. code-block:: bash

  > dolphot <outputname> <options>
  
The **outputname** file is where the photometric catalog will be stored. A number of auxiliary files, using **outputname** as root, will also be created to store additional information and diagnostics. The **options** keywords set the value of a number of parameters used during the PSF-photometry. The parameter values can be set from the command line:

.. code-block:: bash

  > dolphot <outputname> <parametername>=<parametervalue>
  
Any omitted parameter will be set at the default value (cf. `Parameters`_). If we want to specify a large number of parameters, we can store them in a parameter file:

.. code-block:: bash

  > dolphot <outputname> -p<parameterfile>
  
While running, *dolphot* will print diagnostics on the reduction on the standard output. Since these are useful to assess the outcome of the reduction and troubleshoot problems, we may wish to save them in a log file. 

Continuing with our example dataset, we will run the reduction on our M92 images:

.. code-block:: bash

  > dolphot M92_example.phot -pphot.param > phot.log
  
In this example, **phot.param** file contains the following input:

.. code-block:: bash

Nimg = 64
img0_file = jw01334-o001_t001_nircam_clear-f150w_i2d
img0_shift = 0 0
img0_xform = 1 0 0
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
img17_file = jw01334001001_02101_00003_nrca1_cal
img18_file = jw01334001001_02101_00003_nrca2_cal
img19_file = jw01334001001_02101_00003_nrca3_cal
img20_file = jw01334001001_02101_00003_nrca4_cal
img21_file = jw01334001001_02101_00003_nrcb1_cal
img22_file = jw01334001001_02101_00003_nrcb2_cal
img23_file = jw01334001001_02101_00003_nrcb3_cal
img24_file = jw01334001001_02101_00003_nrcb4_cal
img25_file = jw01334001001_02101_00004_nrca1_cal
img26_file = jw01334001001_02101_00004_nrca2_cal
img27_file = jw01334001001_02101_00004_nrca3_cal
img28_file = jw01334001001_02101_00004_nrca4_cal
img29_file = jw01334001001_02101_00004_nrcb1_cal
img30_file = jw01334001001_02101_00004_nrcb2_cal
img31_file = jw01334001001_02101_00004_nrcb3_cal
img32_file = jw01334001001_02101_00004_nrcb4_cal
img33_file = jw01334001001_04101_00001_nrca1_cal
img34_file = jw01334001001_04101_00001_nrca2_cal
img35_file = jw01334001001_04101_00001_nrca3_cal
img36_file = jw01334001001_04101_00001_nrca4_cal
img37_file = jw01334001001_04101_00001_nrcb1_cal
img38_file = jw01334001001_04101_00001_nrcb2_cal
img39_file = jw01334001001_04101_00001_nrcb3_cal
img40_file = jw01334001001_04101_00001_nrcb4_cal
img41_file = jw01334001001_04101_00002_nrca1_cal
img42_file = jw01334001001_04101_00002_nrca2_cal
img43_file = jw01334001001_04101_00002_nrca3_cal
img44_file = jw01334001001_04101_00002_nrca4_cal
img45_file = jw01334001001_04101_00002_nrcb1_cal
img46_file = jw01334001001_04101_00002_nrcb2_cal
img47_file = jw01334001001_04101_00002_nrcb3_cal
img48_file = jw01334001001_04101_00002_nrcb4_cal
img49_file = jw01334001001_04101_00003_nrca1_cal
img50_file = jw01334001001_04101_00003_nrca2_cal
img51_file = jw01334001001_04101_00003_nrca3_cal
img52_file = jw01334001001_04101_00003_nrca4_cal
img53_file = jw01334001001_04101_00003_nrcb1_cal
img54_file = jw01334001001_04101_00003_nrcb2_cal
img55_file = jw01334001001_04101_00003_nrcb3_cal
img56_file = jw01334001001_04101_00003_nrcb4_cal
img57_file = jw01334001001_04101_00004_nrca1_cal
img58_file = jw01334001001_04101_00004_nrca2_cal
img59_file = jw01334001001_04101_00004_nrca3_cal
img1_shift = 0 0
img1_xform = 1 0 0
img1_raper = 2
img1_rchi = 1.5
img1_rsky0 = 15
img1_rsky1 = 35
img1_rsky2 = 3 10
img1_rpsf = 15
img1_apsky = 20 35
FitSky = 2
SigPSF = 5.0
FlagMask = 4
SecondPass = 5
PSFPhotIt = 2
ApCor = 1
FSat = 0.999
NoiseMult = 0.1
WFC3useCTE = 0
RCombine = 1.5
CombineChi = 0
MaxIT = 25
InterpPSFlib = 1
SigFindMult = 0.85
PSFPhot = 1
Force1 = 0
SkySig = 2.25
WFC3UVISpsfType = 0
WFC3IRpsfType = 0
SkipSky = 1
UseWCS = 2
ACSpsfType = 0
ACSuseCTE = 0
PSFres = 1
PosStep = 0.25


  
  
