Draco II
======

NIRcam
--------

NIRISS
--------



HST/ACS
--------

.. _files:
.. _parameter:
.. _preprocessing:
.. _running:
.. _output:
.. _catalogs:
.. _asts:


For this example, we will run DOLPHOT on the HST/ACS F606W and F814W imaging of Draco II taken as part of program GO-14734.

We first examine our files that were downloaded from MAST.

.. code-block:: bash
 
 > pwd
 > photometry/dracoii/acs/
 > ls raw/
 > jdan18010_drc.fits.gz  jdan18bsq_flc.fits.gz  jdan18c0q_flc.fits.gz  jdan19010_drc.fits.gz  jdan19xqq_flc.fits.gz  jdan19xxq_flc.fits.gz
   jdan18boq_flc.fits.gz  jdan18byq_flc.fits.gz  jdan18c5q_flc.fits.gz  jdan19xoq_flc.fits.gz  jdan19xvq_flc.fits.gz  jdan19y1q_flc.fits.gz
 

and then copy and unzip them in the main directory.

.. code-block:: bash
 
 > pwd
 > photometry/dracoii/acs/raw
 > cp *.flc.fits.gz ../
 > cp jdan18010_drc.fits.gz ../
 > cd ..
 > gunzip *.gz
 > ls *flc.fits
 > jdan18boq_f606w_flc.fits  jdan18byq_f606w_flc.fits  jdan18c5q_f606w_flc.fits  jdan19xqq_f814w_flc.fits	jdan19xxq_f814w_flc.fits
   jdan18bsq_f606w_flc.fits  jdan18c0q_f606w_flc.fits  jdan19xoq_f814w_flc.fits  jdan19xvq_f814w_flc.fits	jdan19y1q_f814w_flc.fits
 > ls *drc.fits
 > jdan18010_f606w_drc.fits
 
We now run pre-processing steps.  First is *acsmask*:

.. code-block:: bash

 > acsmask jdan18boq_f606w_flc.fits > phot.log
 > acsmask jdan19xoq_f814w_flc.fits >> phot.log
 ...
 > acsmask jdan18010_f606w_drc.fits >> phot.log
 
next is *splitgroups*:

.. code-block:: bash

 > splitgroups jdan18boq_f606w_flc.fits >> phot.log
 > splitgroups jdan19xoq_f814w_flc.fits >> phot.log
 ...
 > splitgroups jdan18010_f606w_drc.fits >> phot.log
 
The result is a set of fits files with "chip1" and "chip2" in the files names.  
 
.. code-block:: bash

 > ls *chip1.fits
 > jdan18010_f606w_drc.chip1.fits	jdan18byq_f606w_flc.chip1.fits	jdan19xoq_f814w_flc.chip1.fits	jdan19xxq_f814w_flc.chip1.fits
   jdan18boq_f606w_flc.chip1.fits	jdan18c0q_f606w_flc.chip1.fits	jdan19xqq_f814w_flc.chip1.fits	jdan19y1q_f814w_flc.chip1.fits
   jdan18bsq_f606w_flc.chip1.fits	jdan18c5q_f606w_flc.chip1.fits	jdan19xvq_f814w_flc.chip1.fits
 > ls *.chip2.fits
 > jdan18boq_f606w_flc.chip2.fits	jdan18byq_f606w_flc.chip2.fits	jdan18c5q_f606w_flc.chip2.fits	jdan19xqq_f814w_flc.chip2.fits	
   jdan19xxq_f814w_flc.chip2.fits jdan18bsq_f606w_flc.chip2.fits	jdan18c0q_f606w_flc.chip2.fits	jdan19xoq_f814w_flc.chip2.fits
   jdan19xvq_f814w_flc.chip2.fits	jdan19y1q_f814w_flc.chip2.fits
   
Finally, we run *calcsky*:

.. code-block:: bash
 
 > calcsky jdan18boq_f606w_flc.chip1 15 35 -128 2.25 2.00 >> phot.log
 > calcsky jdan18boq_f606w_flc.chip2 15 35 -128 2.25 2.00 >> phot.log
 > calcsky jdan19xoq_f814w_flc.chip1 15 35 -128 2.25 2.00 >> phot.log
 > calcsky jdan19xoq_f814w_flc.chip2 15 35 -128 2.25 2.00 >> phot.log
 ...
 > calcsky jdan18010_f606w_drc.chip1 15 35 -128 2.25 2.00 >> phot.log

The results of *calcsky* are saved as *sky.fits files

.. code-block:: bash

 > ls *sky.fits
 > jdan18010_f606w_drc.chip1.sky.fits  jdan18byq_f606w_flc.chip2.sky.fits	jdan19xoq_f814w_flc.chip2.sky.fits  jdan19xxq_f814w_flc.chip2.sky.fits
   jdan18boq_f606w_flc.chip1.sky.fits  jdan18c0q_f606w_flc.chip1.sky.fits	jdan19xqq_f814w_flc.chip1.sky.fits  jdan19y1q_f814w_flc.chip1.sky.fits
   jdan18boq_f606w_flc.chip2.sky.fits  jdan18c0q_f606w_flc.chip2.sky.fits	jdan19xqq_f814w_flc.chip2.sky.fits  jdan19y1q_f814w_flc.chip2.sky.fits
   jdan18bsq_f606w_flc.chip1.sky.fits  jdan18c5q_f606w_flc.chip1.sky.fits	jdan19xvq_f814w_flc.chip1.sky.fits
   jdan18bsq_f606w_flc.chip2.sky.fits  jdan18c5q_f606w_flc.chip2.sky.fits	jdan19xvq_f814w_flc.chip2.sky.fits
   jdan18byq_f606w_flc.chip1.sky.fits  jdan19xoq_f814w_flc.chip1.sky.fits	jdan19xxq_f814w_flc.chip1.sky.fits


Next, we download the parameter file created for this example.  It can be found `here <xxx>`_.  No modifications of the parameter file are required for this example.

The next step is to execute DOLPHOT.



.. code-block:: bash
 > dolphot dracoii_acs.phot -pphot.param >> phot.log &
 
The 'dracoii_acs.phot' will host the raw photometric output from DOLPHOT.  This name will also serve as the base for other DOLPHOT outputs for this run, e.g., 'dracoii_acs.phot.columns' contains a list of what all the columns in the raw photometry file are.

We found that this run of DOLPHOT took **~XX hours** and used **~YY GB** of RAM.

Once the run is complete, we examine the log file, primarily to look at the alignment staistics.  

.. code-block:: bash
 > cat phot.log
 > 1363 stars for alignment
   image 1:
     coarse alignment = 0.04 -0.03
     429 matched, 389 used, 0.03 -0.03 0.999999 0.00000 -0.000, sig=0.24
   image 2:
     coarse alignment = -0.01 -0.01
     409 matched, 356 used, -0.01 -0.00 1.000009 0.00000 -0.001, sig=0.24
   image 3:
     coarse alignment = 0.04 -0.05
     465 matched, 398 used, 0.03 -0.05 1.000021 0.00000 -0.001, sig=0.24
   image 4:
     coarse alignment = 0.02 0.03
     417 matched, 363 used, 0.02 0.04 1.000021 0.00000 -0.001, sig=0.26
   image 5:
     coarse alignment = 0.04 0.09
     71 matched, 51 used, 0.06 0.11 0.999940 0.00000 -0.002, sig=0.10
    ...
    
The alignment statistics for the first 5 images look pretty good.  Overally, 1363 stars are used as reference stars.  Images 1-4 are aligned to ~0.25 pixels from ~400 matched stars each.  Image 5 has many fewer matched alignment stars (~50) and reports a very good alignment precision of 0.1 pix. Looks earlier in the log file, we see that image 5 (jdan18byq_f606w_flc.chip1.fits) has an integreation time of ~47s, whereas the first 4 images have ~1150s each.  This type of alignment behavior is common when there are such large differences in exposure times.  The rest of the images in the log file show similarly good alignment.

We also check to see if DOLPHOT produced any warnings

.. code-block:: bash
 > cat DracoII_ACS.phot.warnings
 Only 38 aperture stars in image 5, jdan18byq_f606w_flc.chip1 (ACS_F606W, 47.0 sec)
 Only 33 aperture stars in image 6, jdan18byq_f606w_flc.chip2 (ACS_F606W, 47.0 sec)
 Only 34 aperture stars in image 15, jdan19xvq_f814w_flc.chip1 (ACS_F814W, 47.0 sec)
 Only 31 aperture stars in image 16, jdan19xvq_f814w_flc.chip2 (ACS_F814W, 47.0 sec)

Here we see that the short exposures did not have many stars for aperture corrections.  But no other warnings are generated.

We did not generate any diagnostic plots (e.g., PSF residuals) for this example, but based on the alignment alone, we expect ths photometry to be OK.



Creating Stellar Catalogs
------------

* Process to go from .phot file to stellar catalogs
* Depends on use case
 * case of 2 bands
 * case of N bands
* example commands of how to cull catalog
* show example CMDs for 2 and N band criteria

Artificial Star Tests
------------

* Generating AST input list
 * 2 band case
 * N band case
* Running ASTs
 * syntax in parameter file
 * advice (e.g., run in parallel on many cores)
* Suggestions for how to cull ASTs
 * will depend on use case
 
 

