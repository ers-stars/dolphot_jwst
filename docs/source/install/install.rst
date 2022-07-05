.. _requirements:
.. _downloads:
.. _makefile:
.. _compiling:

.. tip::

   Check the `DOLPHOT homepage <http://americano.dolphinsim.com/dolphot/>`_ to make sure you're using the most current version.

Requirements
------------

* C complier (e.g., gcc)
* `PGPLOT <https://sites.astro.caltech.edu/~tjp/pgplot/>`_ (optional) to generate diagnostic plots 
* Fortran complier (optional; e.g., g77, gfortan) to link to PGPLOT

.. note::
   * DOLPHOT can be compiled and run without PGPLOT and Fortan, but it will not be able to generate diagnostic plots.
   * DOLPHOT generally complies fine on UNIX/LINUX/MacOS, but it untested on other operating systems (e.g., Windows).
   * See `this workaround <https://github.com/kazuakiyama/homebrew-pgplot>`_ for installing PGPLOT via `Homebrew <https://brew.sh>`_.

Downloads
------------

All DOLPHOT files can be downloaded from the `DOLPHOT homepage <http://americano.dolphinsim.com/dolphot/>`_.  Files to download and unpack are:

* DOLPHOT base source files
* DOLPHOT module-specific source files
* Pixel Area Maps (PAMs) specific to each camera
* PSF models specific to each camera and filter

.. note::
 Only PAMs and PSF models for the camera(s)/filter(s) of interest need to be downloaded. 

Makefile
------------

The Makefile may require some editing before compiling DOLPHOT.  Here are a few lines to edit

.. code-block:: bash
   
   #export PGHEAD = \"/usr/local/include/cpgplot.h\"
   #export PGPLOT = -L/usr/local/lib -lcpgplot -lpgplot -lpng -L/usr/X11R6/lib -lX11 -L/usr/lib -lgcc
 
 PGPLOT is not linked by default.  To link PGPLOT to DOLPHOT, uncomment these lines and modify the PGPLOT file location as necessary.
 
.. code-block:: bash
   
   #export USEACS=1

Individual camera models are not installed by default.  For example, to install the HST/ACS module, uncomment the above line.
  
.. code-block:: bash
   export CFLAGS+= -DMAXNIMG=100
   export CFLAGS+= -DMAXNSTARS=2000000

DOLPHOT allocates memory based on a pre-set maximum number of images (DMAXNIMG) and stars (DMAXNSTARS). The default values are good for most cases, but if larger number of images or stars are expected, edit these lines in the Makefile. 

.. tip::
 Remeber to re-compile DOLPHOT if the number of images or stars are edited in the Makefile.


Compiling
------------
