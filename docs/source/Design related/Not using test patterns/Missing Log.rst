Missing Log
^^^^^
Definitions:

* setverdict is used with verdict inconc or fail, but without calling log. Inconclusive or unsuccessful test verdicts should be logged, because this helps discovering the reasons for the failure. However, this smell should be classified weak compared to other smells.



Code Example:

.. code-block:: pseudo

  testcase exampleTestCase () runs on ExampleComponent {
    timer t_guard;
    //...
    t_guard.start(10.0);
    alt {
      [] pt.receive(a_MessageOne){
        t_guard.stop
        setverdict(pass)
        pt.send(a_MessageTwo);
      }
      [] any port.receive {
        repeat;
      }
      [] t_guard.timeout {
        setverdict(fail)
        stop;
      }
    }
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

