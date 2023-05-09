Disorder
^^^^^
Definition:

* The sequence of elements within a module does not conform to a given order. A preferred ordering could be:

  #. imports
  #. module parameters
  #. data types
  #. port types
  #. component types
  #. templates
  #. functions
  #. altsteps
  #. test cases
  #. control part


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
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

