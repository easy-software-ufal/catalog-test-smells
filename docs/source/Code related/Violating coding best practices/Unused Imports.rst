Unused Imports
^^^^^
Definitions:

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

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

