Examining the output
============
When *dolphot* has completed running, we need to make sure the reduction run was successful and the photometry reliable. This is done through inspection of the many diagnostic files produced reduction, as well as inspection of the output photometric catalog.

The first file we wish to examine is the log file where we captured *dolphot* standard output. This log contains useful information on about the many steps of the reduction.









When *dolphot* is run with the following syntax:

.. code-block:: bash

  > dolphot <outputname> <options> > <logfile>
  
the output photometric catalog is stored in the **outputname** file. This file contains a output line for each point-source identified during the reduction run. For each line, the **outputname** file contains a long list of outputs. These include photometric measurements and quality flags on each indivual frame, as well as combined photometry from multiple images that use the same filter.
