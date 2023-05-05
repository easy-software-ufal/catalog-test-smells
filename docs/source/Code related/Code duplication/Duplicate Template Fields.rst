Duplicate Template Fields
^^^^^
Definition:

* The fields of two or more templates are identical or very similar


Code Example:

.. code-block:: java

    template MyRecordType t1 := {
    field1 := "foo",
    field2 := 1,
    field3 := true
    }
        

    template MyRecordType t2 := {
    field1 := "foo",
    field2 := 1,
    field3 := true
    }

    template MyRecordType t3 := {
    field1 := "bar",
    field2 := 1,
    field3 := true
    }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

