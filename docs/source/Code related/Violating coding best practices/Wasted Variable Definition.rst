Wasted Variable Definition
^^^^^
Definition:

* A variable is defined and defined again before it is read.

Also Known As:

* Dd Data Flow Anomaly

Code Example:

.. code-block:: pseudo

  function f ( in integer i , out integer j ) {
    var integer k := 1 ;
    k := i ;
    j := k ;
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

