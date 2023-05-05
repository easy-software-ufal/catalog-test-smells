Short Template
^^^^^
Definition:

* Template definition is very short (in terms of characters or number of fields).


Code Example:

.. code-block:: pseudo

  template integer exampleTemplate := 1;

  testcase exampleTestCase() runs on ExampleComponent {
    // ...
    pt.send(exampleTemplate);
    // ...
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

