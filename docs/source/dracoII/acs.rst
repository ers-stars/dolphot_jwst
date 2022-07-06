HST/ACS
=====

.. _files:
.. _parameter:
.. _preprocessing:
.. _running:
.. _output:
.. _catalogs:
.. _asts:


For this example, we will produce run DOLPHOT on the HST/ACS F606W and F814W imaging of Draco II taken as part of program GO-14734.

Files
------------

We first set up a local directory structure that will house the flc and drc files downloaded from MAST and handle the main DOLPHOT operations. 

.. code-block:: bash
 
 > pwd
 > photometry/dracoii/acs/
 > ls
 > raw
 
In this case, DOLPHOT will operate on files in the 'acs' directory and downloaded images will be in the 'raw' subdirectory.

For this dataset, the contents of the raw subdirectory are

.. code-block:: bash
 
 > pwd
 > photometry/dracoii/acs/
 > ls raw/
 > jdan18010_drc.fits.gz  jdan18bsq_flc.fits.gz  jdan18c0q_flc.fits.gz  jdan19010_drc.fits.gz  jdan19xqq_flc.fits.gz  jdan19xxq_flc.fits.gz
   jdan18boq_flc.fits.gz  jdan18byq_flc.fits.gz  jdan18c5q_flc.fits.gz  jdan19xoq_flc.fits.gz  jdan19xvq_flc.fits.gz  jdan19y1q_flc.fits.gz
 

The next step is to copy the raw files up a level to the 'acs' directory.  Because DOLPHOT modifies the fits files, we want to preserve the original files in case we need to re-analyze them.

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
 
.. note::
 DW: In this case, a python script also renamed the files to add the filter name.  We'll have to decide how to include little things (like this) in the documentation.

Preprocessing
------------

The images downloaded from MAST need a few modifications before they can be run through DOLPHOT.  

acsmask
^^^^^^^^^^^^

The first preprocessing step is to run the DOLPHOT utility *acsmask*.  This program masks pixels flagged in the data quality extension (e.g., bad pixels, cosmic rays) and applies the pixel area mask.  It needs to be run on each flc and the drc image.

.. code-block:: bash

 > acsmask jdan18boq_f606w_flc.fits > phot.log
 > acsmask jdan19xoq_f814w_flc.fits >> phot.log
 ...
 > acsmask jdan18010_f606w_drc.fits >> phot.log
 
DOLPHOT reports output to the command line by default.  Here, we've redirected it to a log file 'phot.log' that we'll use to keep track of all DOLPHOT outputs.

splitgroups
^^^^^^^^^^^^

The next preprocessing step is to run the DOLPHOT utility *splitgroups*.  The ACS camera has two chips, 1 and 2.  *splitgroups* creates .fits files for each of the chips.  It needs to be run on each flc and the drc image.

.. code-block:: bash

 > splitgroups jdan18boq_f606w_flc.fits >> phot.log
 > splitgroups jdan19xoq_f814w_flc.fits >> phot.log
 ...
 > splitgroups jdan18010_f606w_drc.fits >> phot.log
 
The result is a set of fits files with "chip1" and "chip2" in the files names
 
.. code-block:: bash

 > ls *chip1.fits
 > jdan18010_f606w_drc.chip1.fits	jdan18byq_f606w_flc.chip1.fits	jdan19xoq_f814w_flc.chip1.fits	jdan19xxq_f814w_flc.chip1.fits
   jdan18boq_f606w_flc.chip1.fits	jdan18c0q_f606w_flc.chip1.fits	jdan19xqq_f814w_flc.chip1.fits	jdan19y1q_f814w_flc.chip1.fits
   jdan18bsq_f606w_flc.chip1.fits	jdan18c5q_f606w_flc.chip1.fits	jdan19xvq_f814w_flc.chip1.fits
 > ls *.chip2.fits
 > jdan18boq_f606w_flc.chip2.fits	jdan18byq_f606w_flc.chip2.fits	jdan18c5q_f606w_flc.chip2.fits	jdan19xqq_f814w_flc.chip2.fits	
   jdan19xxq_f814w_flc.chip2.fits jdan18bsq_f606w_flc.chip2.fits	jdan18c0q_f606w_flc.chip2.fits	jdan19xoq_f814w_flc.chip2.fits
   jdan19xvq_f814w_flc.chip2.fits	jdan19y1q_f814w_flc.chip2.fits
   
Note that there while splitgroups is run on the drc image, only a "chip1" file is produced.

calcsky
^^^^^^^^^^^^

The final preprocessing step is to run the DOLPHOT utility *calcsky*.  *calcsky* makes an initial estimate of the sky and provides smoothed images that are used for initial guesses at star locations.  *calcsky* needs to be run on each image produced by splitgroups, i.e., all chip1 and chip2 files.

.. code-block:: bash
 
 > calcsky jdan18boq_f606w_flc.chip1 15 35 -128 2.25 2.00 >> phot.log
 > calcsky jdan18boq_f606w_flc.chip2 15 35 -128 2.25 2.00 >> phot.log
 > calcsky jdan19xoq_f814w_flc.chip1 15 35 -128 2.25 2.00 >> phot.log
 > calcsky jdan19xoq_f814w_flc.chip2 15 35 -128 2.25 2.00 >> phot.log
 ...
 > calcsky jdan18010_f606w_drc.chip1 15 35 -128 2.25 2.00 >> phot.log

The numerical values in the command line call are described in the DOLPHOT and DOLPHOT ACS module manuals.

.. note::
 DW: how much detail do we want to go into RE the DOLPHOT parameters in these examples? e.g., describe the meanings of ``$r_{in}$``, ``$r_{out}$``, step, ``$\sigma$``, etc.

The results of *calcsky* are saved as *sky.fits files

.. code-block:: bash

 > ls *sky.fits
 > jdan18010_f606w_drc.chip1.sky.fits  jdan18byq_f606w_flc.chip2.sky.fits	jdan19xoq_f814w_flc.chip2.sky.fits  jdan19xxq_f814w_flc.chip2.sky.fits
   jdan18boq_f606w_flc.chip1.sky.fits  jdan18c0q_f606w_flc.chip1.sky.fits	jdan19xqq_f814w_flc.chip1.sky.fits  jdan19y1q_f814w_flc.chip1.sky.fits
   jdan18boq_f606w_flc.chip2.sky.fits  jdan18c0q_f606w_flc.chip2.sky.fits	jdan19xqq_f814w_flc.chip2.sky.fits  jdan19y1q_f814w_flc.chip2.sky.fits
   jdan18bsq_f606w_flc.chip1.sky.fits  jdan18c5q_f606w_flc.chip1.sky.fits	jdan19xvq_f814w_flc.chip1.sky.fits
   jdan18bsq_f606w_flc.chip2.sky.fits  jdan18c5q_f606w_flc.chip2.sky.fits	jdan19xvq_f814w_flc.chip2.sky.fits
   jdan18byq_f606w_flc.chip1.sky.fits  jdan19xoq_f814w_flc.chip1.sky.fits	jdan19xxq_f814w_flc.chip1.sky.fits


Parameter File
------------

Running DOLPHOT
------------

Examining Output
------------

Creating Stellar Catalogs
------------

Artificial Star Tests
------------
