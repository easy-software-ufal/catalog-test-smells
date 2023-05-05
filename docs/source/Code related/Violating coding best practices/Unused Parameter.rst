Unused Parameter
^^^^^
Definitions:

* A parameter is never used within the declaring unit. For in-parameters, the parameter is never read, for out-parameters never defined, for inout-parameters never accessed at all.


Code Example:

.. code-block:: pseudo

  function f ( in integer i , in integer j ) return integer {
    var integer k := 1 ;
    return i + k ;
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

