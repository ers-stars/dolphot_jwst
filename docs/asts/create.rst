Creating Artifical Star Lists
============

A useful capability of DOLPHOT is to perform artifical star tests (ASTs) to evaluate photometric errors, systematic uncertainties and completenss across the CMD. To do so, DOLPHOT injects mock stellar sources in the images, with realistic noise properties, and performs photometry on them using the same set up used for reduction. The first step to perform ASTs is to create a suitable list of input mock stars, that will be injected in the dataset. The input list will consist of multiple entries, one per star, having the following format:

.. code-block:: bash

  1 1 X Y M1 M2 M3...
  1 1 X Y M1 M2 M3...
  1 1 X Y M1 M2 M3...
  ...

Where the first two numbers are the extension number and chip number in the image (both 1, for a typical JWST reduction); X and Y are the pixel coordinate of the mock star, in the coordinate system of the reference image; and the following numbers are the input magnitudes in each of the photometered filters.

.. note::

  The extension number will need to be set to 0, if the frames have been processed through *splitgroups*. This is the case, for instance, is the images are reduced together with HST frames.

ASTs for 2-Band Photometry
-----------------------------

If working with a photometric catalog that only has 2 filters, the input star list can be created by hand or generated using the routine *fakelist*, which uses the following syntax:

.. code-block:: bash

  > fakelist <photname> <filter1> <filter2> <f1min> <f1min> <cmin> <cmax> <options> > <listname>

Where **photname** is the name of the *dolphot* output; **filter1** and **filter2** are the name of the two filters; and **f1min**, **f1max**, **cmin** and **cmax** set the range in magnitude and color of the input mock stars. Commonly used options of *fakelist* include:

* **nstar**: set the number of input stars to be generated. Default is 1.
* **UseXY**: provide the name of a file containing a list of positions (in the format '1 1 X Y'). The generated star list will follow the same spatial probability distribution. Default is uniform spatial distribution.
* **usecmd**: provide a name of a file containing a list of magnitudes (in the format '1 1 X Y Magnitude Color'). The generated star list fill follow the same probability distribution on the CMD. Default is uniform distribution on the CMD.

A practical example of how to use *fakelist* to generate an input star list is provided in the `NIRISS workflow <../examples/m92_niriss.rst>`_

.. tip::

  * **UseXY** can be used to model more accurately the crowding properties of the images. This is, for instance, useful if the field has a strong density gradient.
  * You can use **UseCMD** to improve your computational efficiency, and avoid input stars with unphysical spectral energy distributions (SEDs). Make sure that the input photometry cover the entire SED parameter space that you are trying to characterize

ASTs for Multi-Band Photometry
-----------------------------

If working with more than 2 filters, the recommended procedure is to generate the AST input list outside of DOLPHOT. This can be done in several ways. Distributing the input stars uniformly in the multi-band parameter space is a simple and effective strategy, but it is computationally inefficient, as most input stars have unphysical SEDs. This strategy also requires a very high number of ASTs, especially if working for many filters, to achieve the AST density needed for practical applications. A more efficient solution is to generate the input star photometry using realistic SED models. This can be done using SED fitting codes (such as the BEAST, `Gordon et al. 2016 <https://ui.adsabs.harvard.edu/abs/2016ApJ...826..104G/abstract>`_), or directly sampling stellar evolution models.


In our M92 example, we generate the input star list by sampling a set of stellar isochrones, with a large distribution of ages and metallicities. We then perturbe the photometry by using a scatter of 0.15 mag, to increase our AST coverage and mitigate possible discrepancies between models and observations. We store the input star list in a file called **fake.inputlist**, with the following content:

.. code-block:: bash

  1 1 2266.48  139.33 22.644 21.298 20.863 20.690
  1 1 3283.65 3772.26 27.523 25.788 25.538 24.878
  1 1  609.75  215.64 27.494 26.098 25.423 24.776
  1 1 2257.56 3461.87 25.982 24.199 23.781 22.849
  1 1 1296.89 2335.19 25.591 24.058 23.375 23.208
  1 1 3716.76  348.85 26.783 25.293 24.652 24.181
  1 1  941.47  558.97 18.401 17.536 17.313 17.610
  1 1  714.05 3823.13 28.582 26.655 25.844 24.900
  1 1 1663.79 3586.35 21.612 20.538 20.067 19.936
  1 1  129.95 1751.45 21.009 20.059 19.822 19.691
  1 1 2716.72 2168.35 21.290 20.531 20.140 20.163
  ...

We are now ready to run the ASTs with DOLPHOT.
