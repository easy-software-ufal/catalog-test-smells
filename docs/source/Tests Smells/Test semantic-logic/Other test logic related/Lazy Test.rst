Lazy Test
^^^^^
Definitions:

* More than one test case with the same fixture that tests the same method. This smell affects test maintainability, as assertions testing the same method should be in the same test case. Like EAGER TEST, the original definition [3] leaves some details to interpretation. We consider every call to the class under test as a potential cause of LAZY TEST, irrespective of whether their results are used in an assertion.
* Occurs when multiple test methods invoke the same method of the production object.


Code Example::

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

