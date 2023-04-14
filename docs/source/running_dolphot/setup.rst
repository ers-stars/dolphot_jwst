Setup
========

Once the images have been preprocessed, we are ready to run the PSF-photometry routine. This is invoked with the *dolphot* command, which has the following sintax:

.. code-block:: bash

  > dolphot <outputname> <options>
  
The **outputname** file is where the photometric catalog will be stored. A number of auxiliary files, using **outputname** as root, will also be created to store additional information and diagnostics. The **options** keywords set the value of a number of parameters used during the PSF-photometry. The parameter values can be set from the command line:

.. code-block:: bash

  > dolphot <outputname> <parametername>=<parametervalue>
  
Any omitted parameter will be set at the default value (cf. `Parameters`_). If we want to specify a large number of parameters, we can store them in a parameter file:

.. code-block:: bash

  > dolphot <outputname> -p<parameterfile>
  
While running, *dolphot* will print diagnostics on the reduction on the standard output. Since these are useful to assess the outcome of the reduction and troubleshoot problems, we may wish to save them in a log file. 

Continuing with our example dataset, we will run the reduction on our M92 images:
.. code-block:: bash

  > dolphot M92_example.phot -pphot.param > phot.log
  
In this example, **phot.param** file contains the following input:


  
  
