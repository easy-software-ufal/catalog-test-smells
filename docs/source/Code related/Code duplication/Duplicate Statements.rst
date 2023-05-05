Duplicate Statements
^^^^^
Definition:

* A duplicate sequence of statements in the statement block of one or multiple behavioral entities (functions, test cases and altsteps).


Code Example:

.. code-block:: java

    function f_sendMessages(in float p_duration) runs on ExampleComponent {
        timer t;
        t.start(p_duration);
        t.timeout;
        pt.send("first timeout");
        t.start( p_duration );
        t.timeout;
        pt.send("second timeout " );
    }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

