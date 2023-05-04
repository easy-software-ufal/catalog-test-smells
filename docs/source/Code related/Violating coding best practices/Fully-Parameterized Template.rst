Fully-Parameterized Template
^^^^^
Definitions:

* All fields of a template are defined by formal parameters.


Code Example:

.. code-block::

  type record MyMessageType {
      integer field1,
      charstring field2,
      boolean field3
  }

  template MyMessageType exampleTemplate(integer i, charstring c, boolean b) := {
      field1 := i,
      field2 := c,
      field3 := b
  }

  function f() runs on MyComponent {
      // ...
      p.send(exampleTemplate(42, "dent", true));
      // ...
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

