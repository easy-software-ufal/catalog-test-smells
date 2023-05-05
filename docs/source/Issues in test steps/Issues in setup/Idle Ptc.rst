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

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

