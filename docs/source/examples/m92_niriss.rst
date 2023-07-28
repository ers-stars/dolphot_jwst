M92 NIRISS
======

Here we provide a working example of the reduction of M92 NIRISS data. The workflow is completely analogous to what presented in the main documentation, provided all the relevant NIRCam routines are replaced by the corresponding NIRISS routines.

PRE-PROCESSING
---------------

We start by setting up a directory in which we will perform the NIRISS reduction:

.. code-block:: bash
 
 > pwd
 > photometry/m92/niriss
 > ls
 > raw
 > ls raw/
 >jw01334-o001_t001_niriss_clear-f090w_i2d.fits
 >jw01334-o001_t001_niriss_clear-f150w_i2d.fits
 >jw01334001001_02201_00001_nis_cal.fits
 >jw01334001001_04201_00001_nis_cal.fits
 >jw01334001001_02201_00002_nis_cal.fits
 >jw01334001001_04201_00002_nis_cal.fits

We copy the image of interests in the main reduction directory:

.. code-block:: bash

  > pwd
  > photometry/m92/niriss/raw
  > cp *cal.fits ../
  > cp *i2d.fits ../
  > cd ../
  > ls *cal.fits
  >jw01334001001_02201_00001_nis_cal.fits
  >jw01334001001_04201_00001_nis_cal.fits
  >jw01334001001_02201_00002_nis_cal.fits
  >jw01334001001_04201_00002_nis_cal.fits
  > ls *i2d.fits
  >jw01334-o001_t001_niriss_clear-f090w_i2d.fits
  >jw01334-o001_t001_niriss_clear-f150w_i2d.fits

We run the images through the masking routine:

.. code-block:: bash

  > nirissmask jw01334-o001_t001_niriss_clear-f150w_i2d.fits
  > nirissmask jw01334001001_02201_00001_nis_cal.fits
  > nirissmask jw01334001001_04201_00001_nis_cal.fits
  > nirissmask jw01334001001_02201_00002_nis_cal.fits
  > nirissmask jw01334001001_04201_00002_nis_cal.fits

And calculate the sky maps:

.. code-block:: bash

  > calcsky jw01334-o001_t001_niriss_clear-f150w_i2d 10 25 -64 2.25 2.00
  > calcsky jw01334001001_02201_00001_nis_cal 10 25 -64 2.25 2.00
  > calcsky jw01334001001_04201_00001_nis_cal 10 25 -64 2.25 2.00
  > calcsky jw01334001001_02201_00002_nis_cal 10 25 -64 2.25 2.00
  > calcsky jw01334001001_04201_00002_nis_cal 10 25 -64 2.25 2.00

RUNNING DOLPHOT
-----------

Now that we have pre-processed the images, we can create the photometry parameter file, **phot.param**:

.. code-block:: bash

 Nimg = 4
 img0_file = jw01334-o001_t001_niriss_clear-f150w_i2d
 img1_file = jw01334001001_02201_00001_nis_cal
 img2_file = jw01334001001_02201_00002_nis_cal
 img3_file = jw01334001001_04201_00001_nis_cal
 img4_file = jw01334001001_04201_00002_nis_cal
 
 raper = 3
 rchi = 2.0
 rsky0 = 15
 rsky1 = 35
 rsky2 = 4 10
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

.. note::

 Note that certain keywords (**raper**, **rchi** and **rsky2**) differ from the NIRCam case. Those keywords are camera specific, and should be used following the recommendations of `Weisz et al. 2023 <dud>`
