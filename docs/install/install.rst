.. _requirements:
.. _downloads:
.. _makefile:
.. _compiling:

.. tip::

   Check the `DOLPHOT homepage <http://americano.dolphinsim.com/dolphot/>`_ to make sure you're using the most current version.

Requirements
------------

* C complier (e.g., GCC)
* `PGPLOT <https://sites.astro.caltech.edu/~tjp/pgplot/>`_ (optional) to generate diagnostic plots 
* Fortran complier (optional; e.g., g77, gfortan) to link to PGPLOT

.. note::
   * DOLPHOT can be compiled and run without PGPLOT and Fortran, but it will not be able to generate diagnostic plots.
   * DOLPHOT generally complies fine on UNIX/LINUX/MacOS, but it untested on other operating systems (e.g., Windows).
   * For Mac, PGPLOT is available via package managers like `Macports <https://www.macports.org>`_ and `Homebrew <https://brew.sh>`_.
   * See `this workaround <https://github.com/kazuakiyama/homebrew-pgplot>`_ for installing PGPLOT via Homebrew.
   * The main plots generated by PGPLOT are PSF residuals, which can be generated manually using the PSF residual files created by DOLPHOT.
   
   

Downloads
------------

All DOLPHOT files can be downloaded from the `DOLPHOT homepage <http://americano.dolphinsim.com/dolphot/>`_.  Files to download and unpack are:

* DOLPHOT base source files
* DOLPHOT module-specific source files
* PSF models specific to each camera and filter


Makefile
------------

The Makefile may require some editing before compiling DOLPHOT.  Here are a few lines to edit

.. code-block:: bash
   
   #export PGHEAD = \"/usr/local/include/cpgplot.h\"
   #export PGPLOT = -L/usr/local/lib -lcpgplot -lpgplot -lpng -L/usr/X11R6/lib -lX11 -L/usr/lib -lgcc
 
PGPLOT is not linked by default.  To link PGPLOT to DOLPHOT, uncomment these lines and modify the PGPLOT file location as necessary.
 
.. code-block:: bash
   
   #export USENIRCAM=1

Individual camera models are not installed by default.  For example, to install the NIRCAM module, uncomment the above line.
  
.. code-block:: bash

   export CFLAGS+= -DMAXNIMG=100
   export CFLAGS+= -DMAXNSTARS=2000000

DOLPHOT allocates memory based on a pre-set maximum number of images (DMAXNIMG) and detections (DMAXNSTARS). The default values are good for most cases, but if larger number of images or detections are expected, edit these lines in the Makefile. 

.. tip::
   Remeber to re-compile DOLPHOT if the number of images or detections is edited in the Makefile.


Compiling
------------

To compile DOLPHOT, enter the DOLPHOT directory and type:

.. code-block:: bash

   make
   
.. note::
  *  Some compliers may throw warnings, but these do not generally affect the DOLPHOT installation. 
  *  Errors reported during compiling will prevent DOLPHOT from running correctly or at all.
  * DOLPHOT can be built using a number of different C compilers (e.g., GCC, ICC). However, due to differences in floating point math treatment, DOLPHOT      output can show minor differences depending on the compiler used. During our testing, we have found the GCC compiler to be the most adeherent to IEEE floating point standards and, therefore, recommend it for DOLPHOT installation.
  
.. tip::  
  *  It is recommended to add the "bin" subdirectory of DOLPHOT to your system PATH environment.
  
Using custom PSF models
------------

Pre-computed PSF models are available for download on the `DOLPHOT homepage <http://americano.dolphinsim.com/dolphot/>`_. These include up-to-date NIRCam and NIRISS PSF models. These models have been generated with `WebbPSF <https://webbpsf.readthedocs.io/en/latest/>`_ v1.2.1, and have the following characteristics:

* Detector position: 5x5 spatial grid distributed uniformly on each of the chips.
* PSF FoV: 51x51 px square FoV
* Spatial oversampling factor: 5
* Number of used wavelengths: 21 for W filters, 9 for M filters and 5 for N filters, sampling flux from a G5V Phoenix atmosphere model.
* Optical Path Delay (OPD) map from Jul. 24th, 2022 (O2022072401-NRCA3_FP1-1.fits).

However, users who want to use different PSF grids (e.g., to use different OPD maps) can do so with help of the *nircammakepsf/nirissmakepsf* routines. First, we create a 'tmp' subdirectory in the DOLPHOT folder:

.. code-block:: bash
 
 > pwd
 > ~/dolphot2.0/
 > mkdir tmp

Then we place a folder, containing our preferred PSF models, in the 'tmp' directory. As of writing, *nircammakepsf* and *nirissmakepsf* can ingest standard output from WebbPSF, in .fits file format:

.. code-block:: bash
 
 > cd tmp
 > cp ~/PSFpath/MyPSFs ./

.. note::
   The recommended WebbPSF settings to create DOLPHOT-compatible PSFs are: fov=51, num=25, oversample=5, add_distortion=True, detsampled=False, norm='exit_pupil'

Finally, we run *nircammakepsf/nirissmakepsf* specifying the desired filter and the PSF grid to use. The routine will convert the requested PSFs to binary files that are ready to use with DOLPHOT. The binary psfs will be located in the 'dolphot2.0/nircam/data/' or 'dolphot2.0/niriss/data/' subdirectory. For instance, if we want to create new PFSs for the NIRCam F090W filter:

.. code-block:: bash

   >cd ../
   > nircammakepsf F090W -base=MyPSFs
   > ls nircam/data
   > F090W.nrca1.psf
   > F090W.nrca2.psf
   > F090W.nrca3.psf
   > F090W.nrca4.psf
   > F090W.nrcb1.psf
   > F090W.nrcb2.psf
   > F090W.nrcb3.psf
   > F090W.nrcb4.psf
 
Repeat the process for every filter of interest. DOLPHOT is now set up to work with the new PSF grid.
 
.. tip::

   You can store different binary PSF grids and replace the files in 'nircam/data/' or 'niriss/data' every time you want to change PSFs. DOLPHOT does not need to be recompiled after you change PSFs.
   
.. note::
   Similar routines (e.g., *acsmakepsf*, *wfc3makepsf*) exist to create binary PSF files for the HST instruments, starting from `Tiny Tim <https://www.stsci.edu/hst/instrumentation/focus-and-pointing/focus/tiny-tim-hst-psf-modeling>`_ output. Usage and syntax is analogous to *nircammakepsf*.
 
