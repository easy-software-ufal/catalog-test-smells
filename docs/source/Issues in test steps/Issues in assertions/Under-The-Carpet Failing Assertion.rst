Under-The-Carpet Failing Assertion
^^^^^
Definitions:

* A test having the smell Under-the-carpet failing Assertion is a test that returns a successful test-result, but contains hidden assertions. A hidden assertion is an assertion that is put into comments, is not executed when the test runs, and which would actually throw an Error or Failure if the comment were removed.


Code Example:

References:

 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_
 * `Rule-based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_

