Examining the output
============
When *dolphot* is run with the following syntax:

.. code-block:: bash

  > dolphot <outputname> <options> > <logfile>
  
the output photometric catalog is stored in the **outputname** file. This file contains a output line for each point-source identified during the reduction run. For each line, the **outputname** file contains a long list of outputs. These include photometric measurements and quality flags on each indivual frame, as well as combined photometry from multiple images that use the same filter.
