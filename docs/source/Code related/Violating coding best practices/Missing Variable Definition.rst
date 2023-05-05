Missing Variable Definition
^^^^^
Definition:

* A variable or out parameter is read before its value has been defined. Access to undefined variables might result in unpredictable behavior.

Also Known As:

* Ur Data Flow Anomaly

Code Example:

.. code-block:: pseudo

  function f (in integer i, out integer j) {
    var integer k := 1, l;
    j := i + j + k + l;
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

