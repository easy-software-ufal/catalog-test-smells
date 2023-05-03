Sensitive Equality
^^^^^
Definitions:

* A test case with an assertion that compares the state of objects by means of their textual representation, i.e., by means of the result of toString().
* van Deursen et al. [18] state the agility and ease to write equality checks using the toString() method, being a frequent alternative to calculate a result value and map it to a sequence to compare to a literal string representing the expected value. However, these tests can depend on many irrelevant details, such as commas,  quotes, and spaces. And whenever the toString() method for an object is changed, all related tests will start to fail.
* When an test checks for equality through the use of the toString method.
* Occurs when the toString method is used within a test method. Test methods verify objects by invoking the default toString() method of the object and comparing the output against an specific string. Changes to the implementation of toString() might result in failure. The correct approach is to implement a custom method within the object to perform this comparison.


Code Example::

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

