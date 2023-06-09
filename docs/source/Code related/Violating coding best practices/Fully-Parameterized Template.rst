Fully-Parameterized Template
^^^^^
**Definition:**

* All fields of a template are defined by formal parameters.


**Code Example:**

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


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
* `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_
