Calculating the Sky
==========
After pre-processing the frames with the *mask* routines (and splitting multi-chip frames with *splitgroup*, if necessary), the last step before running PSF-photometry is to calculate a sky image for each of our frames. This is done through the routine *calcsky*, which has syntax:

.. code-block:: bash

  > calcsky <fits base> <rin> <rout> <step> <σ low> <σ high>

The sky computation is made by taking all pixels in an annulus around the pixel in question. The annulus extends from **rin** to **rout** pixels from the pixel whose value is being measured, and is sampled every **step** pixels. While **step** = 1 will always work, one can typically set **step** to the PSF size and achieve equally good results. The algorithm is a mean with iterative rejection. Each iteration, the mean and standard deviation are calculated, and values falling more than **σ low** below or **σ high** above the mean are rejected. This procedure continues until no pixels are rejected. After an initial sky map is calculated, it is boxcar smoothed with a kernel of size **step**. *Calcsky* can run in an alternative mode, which is signaled by setting **step** to a negative number. This option will divide the image into squares of size **−step** pixels on a side and run the iterative rejection algorithm on each square. The resulting value is assigned to the central pixel of the square, and the sky map is created by interpolation. When this option is used, **rin** and **rout** are ignored. The resulting sky image is a FITS file named **<fits base>**.sky.fits.

.. tip::
  While DOLPHOT can be set up to use the *calcsky* map as final sky measurement, it is usually better to calculate local sky measurement around each source, during the PSF-photometry run itself. In the latter case, the *calcsky* map is only used as a first guess, and less accuracy is required in this step. For a 2k x 2k px detector, setting **step** to values of -64 or -128 is generally sufficient to achieve good measurements.
  
In our M92 example, we are going to execute *calcsky* on the reference image:

.. code-block:: bash

  > calcsky jw01334-o001_t001_nircam_clear-f150w_i2d 10 25 -64 2.25 2.00
  
And on each of the CRF files:

.. code-block:: bash

  > calcsky jw01334001001_02101_00001_nrca1_o001_crf 10 25 -64 2.25 2.00
  > calcsky jw01334001001_02101_00001_nrca2_o001_crf 10 25 -64 2.25 2.00
  > calcsky jw01334001001_02101_00001_nrca3_o001_crf 10 25 -64 2.25 2.00
  ...


