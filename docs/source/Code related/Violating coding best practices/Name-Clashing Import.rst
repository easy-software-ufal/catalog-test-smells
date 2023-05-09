Name-Clashing Import
^^^^^
Definition:

* An imported element causes a name clash with a declaration in the importing module or another imported element.


Code Example:

.. code-block:: javascript

  module Foo {
    const charstring MY_CONST := "foo";
  }

  module Bar {
    import from Foo all;

    const charstring MY_CONST := "bar";

    function f(in charstring s) return boolean {
      if (MY_CONST == s) {
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

