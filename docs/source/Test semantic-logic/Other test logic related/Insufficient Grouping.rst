Insufficient Grouping
^^^^^
Definitions:

* A module or group contains too many elements. Especially for large modules, groups should be used to add logical structure to the module and enhance readability. If a group reaches a critical size, it can be structured further by subgroups.


Code Example:

.. code-block::

 module InsufficientGrouping {
  type record myRecordType1 { // . . .
  }

  type record myRecordType2 { // . . .
  }

  type record myRecordType3 { // . . .
  }

  type record myRecordType4 { // . . .
  }

  type record myRecordType5 { // . . .
  }

  template myRecordType1 myTemplate1 := { // . . .
  }

  template myRecordType1 myTemplate2 := { // . . .
  }

  template myRecordType1 myTemplate3 := { // . . .
  }

  template myRecordType1 myTemplate4 := { // . . .
  }

  template myRecordType1 myTemplate5 := { // . . .
  }

  function f1( ) { // . . .
  }

 // more declarations here
 }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

