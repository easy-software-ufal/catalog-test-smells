Duplicate Local Variable/Constant/Timer
^^^^^
Definitions:

* The same local variable, constant or timer is defined in two or more functions, test cases or altsteps running on the same component.


Code Example:

.. code-block:: java

    type component c {
        port ExamplePort p;
    }
    testcase tc1() runs on c {
        timer t;
        p.send("foo1");
        t.start (10.0);
        alt {
            [] p.receive("bari") {
            // do something
            }
            [] any port.receive{
            // error handling
            }
            [] t.timeout {
            // error handling
            }
        }
    }
    testcase tc2() runs on c {
        timer t;
        p.send("foo2");
        t.start (20.0);
        alt {
            [] p.receive("bar2") {
            // do something
            }
            [] any port.receive {
            // error handling
            }
            [] t.timeout {
            // error handling
            }
        }
    }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

