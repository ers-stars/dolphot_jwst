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
   * Here is `A workaround <https://github.com/kazuakiyama/homebrew-pgplot>`_ for installing PGPLOT via `Homebrew <https://brew.sh>`_.

Downloads
------------

All DOLPHOT files can be downloaded from the `DOLPHOT homepage <http://americano.dolphinsim.com/dolphot/>`_.  Files to download and unpack are:

* DOLPHOT base source files
* DOLPHOT module-specific source files
* Pixel Area Maps specific to each camera
* PSF models specific to each camera and filter

Makefile
------------

Compiling
------------
