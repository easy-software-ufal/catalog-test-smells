Duplicate In-Line Templates
^^^^^
Definitions:

* Two or more similar or identical in-line templates.


Code Example::

.. code-block:: java

    module DuplicateInlineTemplates (
        type record ExampleRecordType (
            boolean exampleField1,
            integer exampleField2,
            charstring exampleField3
    }
    type port ExamplePort message (
        out ExampleRecordType;

    }
    type component ExampleComponent (
        port ExamplePort pt;
    }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

