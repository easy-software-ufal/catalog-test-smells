Unused Imports
^^^^^
Definition:

* An import from another module is never used.


Code Example:

.. code-block:: ruby

  module Foo {
    const charstr ing FOO CONST := " foo " ;
  }

  module Bar {
    const charstr ing BAR CONST := " bar " ;
  }

 module Baz {
  import from Foo all;
  import from Bar all;

  function f ( in charstring s ) return boolean {
    if (FOO_CONST == s ) {
      return true;
    }

    return false;
  }
 }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_ :octicon:`graph;1em`

