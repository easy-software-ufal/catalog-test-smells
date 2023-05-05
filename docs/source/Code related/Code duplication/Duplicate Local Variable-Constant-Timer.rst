Duplicate Local Variable/Constant/Timer
^^^^^
Definition:

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
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

