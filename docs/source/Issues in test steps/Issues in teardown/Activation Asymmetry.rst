Activation Asymmetry
^^^^^
Definition:

* A default activation has no matching subsequent deactivation in the same statement block, or a deactivation has no matching previous activation.


Code Example:

.. code-block:: pseudo

  altstep myAltstep (timer t) runs on MyComponent {
    [] any port.receive {
      setverdict(fail)
      log ("unexpected message")
    }
    [] t.timeout{
      setverdict(fail)
      log("timeout")
    }
  }

  function activateDefault(timer t) return default {
    // no deactivation in this function!
    return act ivate ( myAltstep ( t ) )
  }

  testcase myTestcase1 ( ) runs on MyComponent {
    timer t
    var default myDefaultVar := activate(myAltstep(t))
    t.start(10.0)
    alt{
      [] p.receive(charstring:("foo1")){
        p.send("ack")
      }
      [] p.receive(charstring:("bar1")) {
        p.send("nack")
      }
    }
    deactivate(myDefaultVar)
  }

 testcase myTestcase2 () runs on MyComponent {
  timer t;
  // activation in function call
  var default myDefaultVar := activateDefault(t)
    t.start(10.0)
    alt {
      []p.receive(charstring:("foo2")) {
        p.send("ack")
      }
      []p.receive(charstring:("bar2")) {
        p.send("nack")
      }
    }
    deactivate (myDefaultVar)
  }

  testcase myTestcase3 ( ) runs on MyComponent {
    // deactivation in different statement blocks
    timer t
    var default myDefaultVar
    myDefaultVar := activate(myAltstep(t))
    t.start(10.0)

    if(2 > 1) {
      alt {
        [] p.receive(charstring:("foo5")){
          p.send("ack")
        }[] p.receive(charstring:("bar5")){
          p.send("nack")
        }
      }
      deactivate ( myDefaultVar )
    }
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_ :octicon:`graph;1em`

