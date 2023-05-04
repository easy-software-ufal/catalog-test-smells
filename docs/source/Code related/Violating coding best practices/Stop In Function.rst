Stop In Function
^^^^^
Definitions:

* A function contains a stop statement. If possible, functions should not contain any stop statement, because this can prevent the execution of postambles (e.g. code that has to be executed after each test case). Instead, functions should use return values. However, this smell should be classified weak compared to other smells.


Code Example:

.. code-block:: pseudo

  function f() {
    timer t := 50;
    t.start();

    alt {
      [] p.receive("foo") {
        t.stop;
        setverdict(pass);
      }
      [] t.timeout {
        setverdict(inconc);
        stop;
      }
    }
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

