Singular Component Variable/Constant/Timer Reference
^^^^^
Definition:

* A component variable, constant or timer is referenced by one single function, test case or altstep only, although other behavioral entities run on the component as well.

Code Example:

.. code-block:: pseudo

  module SingularComponentVCTReference {
    type port ExamplePort message {
      inout charstring;
    }

    type component c {
      timer t;
      port ExamplePort p;
    }

    function f() runs on c {
      p.send("bar");
      p.send("baz");
    }

    testcase tc() runs on c {
      t.start(10.0);
      alt {
        [] p.receive("foo") {
          p.send("bar");
        }
        [] any port.receive {
          // error handling
        }
        [] t.timeout {
          // error handling
        }
      }
    }
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

