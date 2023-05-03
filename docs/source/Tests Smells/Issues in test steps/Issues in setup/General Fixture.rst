General Fixture
^^^^^
Definitions:

* A test fixture that is too general. Ideally, test cases should use all the fields provided by their fixture. This might be difficult to uphold when the fixture is shared by several test cases.
* When the fixture is then reused and augmented by each test to create the necessary setup
* The test is building or referencing a larger fixture than is needed to verify the functionality in question.
* A test fixture that is too general. Ideally, test cases should use all the fields provided by their fixture. This might be difficult to uphold when the fixture is shared by several test cases.
* Occurs when a test case fixture is too general and the test methods only access part of it. A test setup/fixture method that initializes fields that are not accessed by test methods indicates that the fixture is too generalized. A drawback of it being too general is that unnecessary work is being done when a test method is run.


Code Example::

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Let’s not <https://thoughtbot.com/blog/lets-not>`_
 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_
 * `SoCRATES: Scala radar for test smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

