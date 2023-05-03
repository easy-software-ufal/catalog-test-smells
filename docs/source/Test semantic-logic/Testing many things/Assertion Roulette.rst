Assertion Roulette
^^^^^
Definitions:

* A test case that contains more than one assertion of which at least one does not provide a reason for assertion failure. In case the test fails, this test smell encumbers identifying which assertion failed and the reason why
* In test cases affected by this smell, it is hard to tell which of several assertions failed.
* collection of unexplained assertions in a single test method that makes it difficult to trace which exact assertion had a problem in the event of test failure
* A test that has multiple assertion statements that do not provide any description of why they failed
* Occurs when a test method has multiple non-documented assertions. Multiple assertion statements in a test method without a descriptive message impacts readability/understandability/maintainability as it’s not possible to understand the reason for the failure of the test.
* When a test method has many unexplained assertions, making it hard to tell which one may cause a test failure


Code Example::

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `Test Artifacts — The Practical Testing Book <https://damorimrg.github.io/practical_testing_book/goodpractices/artifacts.html>`_

