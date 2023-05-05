Missing Verdict
^^^^^
Definition:

* A test case does not set a verdict. Normally a test case should set a verdict before terminating.


Code Example:

.. code-block:: pseudo

  testcase exampleTestCase ( ) runs on ExampleComponent {
    timer tguard;
    // . . .
    tguard.start(10.0);
    alt {
        [] pt.receive(aMessageOne) {
            tguard.stop;
            setverdict(pass);
            pt.send(aMessageTwo);
        }
        [] anyport.receive {
            repeat;
        }
        [] tguard.timeout {
            stop;
        }
    }
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

