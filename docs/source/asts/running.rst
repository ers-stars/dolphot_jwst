Running Artifical Stars
==========

Once we have a mock star input list, we can perform ASTs on our dataset. This is done by calling again the routine *dolphot*, using the following syntax:

.. code-block:: bash

  dolphot <photname> -p<fakeparam> > fake.log

Where **photname** is the name of the photometric catalog from the original *dolphot* run. The file **fakeparam** is identical to the parameter file of the original *dolphot* run, but has additional keywords:

* **FakeStars**: If this keyword is set, *dolphot* will run in artificial star mode. This parameter should be set to the name of the artifical star input list.
* **Fakeout**: Specify output file created when running artificial stars. If not specified, default is the same filename as the original photometry, with a “.fake” suffix appended.
* **FakeMatch** = 3.0: Maximum allowable distance (in pixels) between input and recovered artificial star.
* **FakePSF** = 1.5: Approximate FWHM of an SNR map of the reference image, used to determine which of two input stars a recovered star should be matched with. This value should be approximately set to the FWHM of the image multiplied by the square root of two; however setting simply to the FWHM of the image is suitable if the crowding output value is used as a goodness of fit metric.
* **FakeStarPSF** = 0: Use PSF residual from initial photometry run. This should be left at zero, unless the PSF residuals are small and well-measured.
* **FakePad** = 0: Define how far an artificial star must be inside the bounds of at least one of the images being used. Zero means that the star will be used if its center falls within any of the images. Negative values allow stars whose centers are outside all images to be used.
* **RandomFake** = 1: Apply Poisson noise to fake stars when adding them. This should always be used, unless running fake star tests twice (once with and once without) to quantify photometric errors from crowding and background independently of the errors due to photon noise.

In our M92 example, we run ASTs by calling:

.. code-block:: bash

  dolphot M92_example.phot -pfake.param > fake.log

With the file **fake.param** having the following content:

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

  FakeStars = fake.inputlist
  FakeOut = M92_example.fake
  RandomFake = 1
  FakeMatch = 3.0
  FakePad = 0
  FakeStarPSF = 0
  FakePSF = 1.5

This way, *dolphot* will inject the mock stars, one at the time, in the images and measure its properties. The output file, **M92_example.fake** will contain an entry for each artifical star successfully processed (this might be slightly lower than the number of stars in the input list). For each star, the output will consist of the same columns present in the original photometry file, preceeded by a number of additional columns listing the input paramters of the mock star in each image.
