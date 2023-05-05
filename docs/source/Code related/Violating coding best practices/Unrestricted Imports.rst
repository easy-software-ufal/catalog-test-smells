Unrestricted Imports
^^^^^
Definitions:

* A module imports more from another module than needed.


Code Example:

.. code-block:: ruby

  module Foo {
    group groupConstants {
    const charstr ing FOO CONST := " foo " ;
      // some other constants . . .
    }

    group groupTypes {
      // type definitions . . .
    }

    group groupComponents {
      // component definitions . . .
    }
  }

 module Baz {
  import from Foo all;

  function f ( in charstring s ) return boolean {
    if (FOO_CONST == s ) {
      return true;
    }

    return false;
  }
 }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

