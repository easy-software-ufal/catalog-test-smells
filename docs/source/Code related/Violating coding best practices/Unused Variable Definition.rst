Unused Variable Definition
^^^^^
Definition:

* A defined variable or in parameter is not read before it becomes undefined.

Also Known As:

* Du Data Flow Anomaly

Code Example:

.. code-block:: pseudo

  function f ( in integer i , out integer j ) {
    var integer k := 1;
    j := 1;
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

