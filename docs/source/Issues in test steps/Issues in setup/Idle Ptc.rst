Idle Ptc
^^^^^
Definition:

* A PTC is created but never started. A PTC which is not started is of no use for the test case.


Code Example:

.. code-block:: pseudo

  testcase exampleTestCase ( ) runs on MainComponentType system SystemType {
    //...
    var ParallelComponentType exampleComponent := ParallelComponentType.create;
    map(self: aPort, system: aPort) ;
    connect(self: anotherPort, exampleComponent: aPort ) ;
    // no start here...
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

