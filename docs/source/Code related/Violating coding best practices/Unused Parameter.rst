Unused Parameter
^^^^^
Definition:

* A parameter is never used within the declaring unit. For in-parameters, the parameter is never read, for out-parameters never defined, for inout-parameters never accessed at all.


Code Example:

.. code-block:: pseudo

  function f ( in integer i , in integer j ) return integer {
    var integer k := 1 ;
    return i + k ;
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

