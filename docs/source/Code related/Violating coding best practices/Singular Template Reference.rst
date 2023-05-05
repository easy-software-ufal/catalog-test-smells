Singular Template Reference
^^^^^
Definitions:

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

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

