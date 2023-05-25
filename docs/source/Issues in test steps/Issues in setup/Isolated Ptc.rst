Isolated Ptc
^^^^^
**Definition:**

* A PTC is created and started, but neither connected to another component nor mapped to the TSI. A PTC which is not connected or mapped is isolated from all other components, especially the MTC, and is of no use for the test.


**Code Example:**

.. code-block:: pseudo

  testcase exampleTestCase() runs on MainComponentType system SystemType {
    // . . .
    var ParallelComponentType exampleComponent := ParallelComponentType.create;
    // no map or connect statement shere!
    exampleComponent.start(exampleBehavior())
    exampleComponent.done
    // . . .
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_
