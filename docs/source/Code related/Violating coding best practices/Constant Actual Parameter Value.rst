Constant Actual Parameter Value
^^^^^
Definition:

* The value of an actual parameter is the same for all occurances. In contrast to Unused Parameter (4.3.1), the parameter is in use within the declaring entity and must not simply be removed. The declaring entity could be a template or a behavioral entity (function, test case or altstep).


Code Example:

.. code-block::

  template myType t (charstring p1, integer p2) := {
    field1 := true,
    field2 := p2,
    field3 := p1
  }

  function f() runs on myComponent {
    // ...
    p.send(templateA("foo", 42));
    // ...
    p.send(templateA("foo", 42));
    // ...
    p.send(templateA("foo", 43));
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

