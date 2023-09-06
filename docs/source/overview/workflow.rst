DOLPHOT Workflow
==========

For most use cases, the process of applying DOLPHOT to NIRCam or NIRISS images is fairly straightforward.  The main steps are

#. Download and install DOLPHOT base sources and separately download DOLPHOT sources for relevant modules (e.g., NIRCam, NIRISS, HST -- if doing cross-facility photometry)
#. Download and install PSF models for relevant cameras and filters
#. Download the images (JWST, HST) of interest from MAST
#. Use the masking utilities from DOLPHOT to mask bad pixels in the JWST images
#. Set up your DOLPHOT parameter file
#. Run DOLPHOT
#. Use various photometric quality metrics to keep likely stars and reject contamination (e.g,. background galaxies, diffraction spikes)
#. Run artifical star tests to quantify uncertainties

Though there are many possible variations in each step, the purpose of this JWST ERS program is to provide guidance for how to do very good photometry without needing to make any (or many) adjustments.  
