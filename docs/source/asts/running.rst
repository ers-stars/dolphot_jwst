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
