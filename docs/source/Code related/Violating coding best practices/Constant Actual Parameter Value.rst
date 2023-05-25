Constant Actual Parameter Value
^^^^^
**Definition:**

* The value of an actual parameter is the same for all occurances. In contrast to Unused Parameter (4.3.1), the parameter is in use within the declaring entity and must not simply be removed. The declaring entity could be a template or a behavioral entity (function, test case or altstep).


**Code Example:**

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

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
* `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_
