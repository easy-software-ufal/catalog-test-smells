Missing Variable Definition
^^^^^
Definitions:

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

