Singular Template Reference
^^^^^
Definition:

* A template definition is referenced only once.


Code Example:

.. code-block:: pseudo

  template MyMessageType exampleTemplate := {
    field1 := omit,
    field2 := "foo",
    field3 := true
  }

  testcase exampleTestCase() runs on ExampleComponent {
    // ...
    pt.send(exampleTemplate);
    // ...
  }

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_ :octicon:`graph;1em`

