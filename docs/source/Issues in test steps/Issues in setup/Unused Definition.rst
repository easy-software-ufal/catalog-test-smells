Unused Definition
^^^^^
Definition:

* Unused code should be removed. Note that only local definitions can be removed safely because they cannot be accessed from outside the defining unit. For global definitions there might exist references in modules which have not been considered.


Code Example:

.. code-block:: pseudo

  function unused_f ( in integer i ) return integer {
    var integer j := 4 2 , k ;
    return i + j ;
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

