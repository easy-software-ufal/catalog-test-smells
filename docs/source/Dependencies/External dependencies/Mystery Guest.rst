Mystery Guest
^^^^^
Definitions:

* A test case that uses external resources that are not managed by a fixture. A drawback of this approach is that the interface to external resources might change over time necessitating an update of the test case, or that those resources might not be available when the test case is run, endangering the deterministic behavior of the test.
* The test reader is not able to see the cause and effect between fixture and verification logic because part of it is done outside the Test Method.
* The test reader is not able to see the cause and effect between fixture and verification logic because part of it is done outside the Test Method.
* The test reader is not able to see the cause and effect between fixture and verification logic because part of it is done outside the Test Method.
* Occurs when a test method utilizes external resources (e.g. files, database, etc.). Use of external resources in test methods will result in stability and performance issues. Developers should use mock objects in place of external resources.


Code Example:

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Let’s not <https://thoughtbot.com/blog/lets-not>`_
 * `Mystery Guest <https://thoughtbot.com/blog/mystery-guest>`_
 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

