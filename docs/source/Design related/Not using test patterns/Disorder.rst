Disorder
^^^^^
Definition:

* The sequence of elements within a module does not conform to a given order. A preferred ordering could be:

  * imports
  * module parameters
  * data types
  * port types
  * component types
  * templates
  * functions
  * altsteps
  * test cases
  * control part


Code Example:

.. code-block:: pseudo

  function f() {
    //...
  }

  type record exampleRecordType {
    //...
  }

  template exampleRecordType t :=  {
    //...
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

