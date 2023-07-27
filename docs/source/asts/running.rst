Running Artifical Stars
==========

Once we have a mock star input list, we can perform ASTs on our dataset. This is done by calling again the routine *dolphot*, using the following syntax:

.. code-block:: bash

  dolphot <photname> -p<fakeparam> > fake.log

Where **photname** is the name of the photometric catalog from the original *dolphot* run. The file **fakeparam** is identical to the parameter file of the original *dolphot* run, but has additional keywords:

* **FakeStars**: If this keyword is set, 
* **Fakeout**:
* **FakeMatch** = 3.0:
* **FakePSF** = 1.5:
* **FakeStarPSF** = 0:
* **FakePad** = 0:
* **RandomFake** = 1:
