Setup
========

Once the images have been preprocessed, we are ready to run the PSF-photometry routine. This is invoked with the *dolphot* command, which has the following sintax:

.. code-block:: bash
  > dolphot <outputname> <options>
  
The **outputname** file is where the photometric catalog will be stored. A number of auxiliary files, using **outputname** as root, will also be created to store additional information and diagnostics. The **options** keywords set the value of a number of parameters used during the PSF-photometry. The parameter values can be set from the command line:

.. code-block:: bash
  > dolphot <outputname> <parametername>=<parametervalue>
  
  Any omitted parameter will be set at the default value. If we want to 
