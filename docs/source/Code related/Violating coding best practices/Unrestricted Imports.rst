Unrestricted Imports
^^^^^
Definition:

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
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_ :octicon:`graph;1em`

