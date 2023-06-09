Under-The-Carpet Failing Assertion
^^^^^
**Definition:**

* A test having the smell Under-the-carpet failing Assertion is a test that returns a successful test-result, but contains hidden assertions. A hidden assertion is an assertion that is put into comments, is not executed when the test runs, and which would actually throw an Error or Failure if the comment were removed.

**Also Known As:**

* Commented Code in the Test

**Code Example:**

.. code-block:: smalltalk

  ICImporterTest >> #testImport
    ...
    self assert: eventAtDate textualDescription = 'blabla'"
    self assert: eventAtDate categories anyOne
    = (calendar categoryWithSummary: 'business').
    "self assert: ...


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Rule-based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
