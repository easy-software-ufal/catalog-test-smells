Bad Naming
^^^^^
Definition:

* When a test fails, or when the test base requires maintenance, the test names are the first thing developers will generally attempt to understand before they apply changes to the test or the code being tested. If test names are poor quality, developers will need to spend time reading the code and determining how the test’s actual behavior is related to its name


Code Example:

.. code-block:: pseudo

  function calculateSomething() {
    // ...
  }

  function calculateSomethingElse() {
    // ...
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Test Naming Failures. An Exploratory Study of Bad Naming Practices in Test Code <https://scholarworks.rit.edu/theses/11053/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_
 * `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_

