Unreachable Default
^^^^^
Definition:

* An alt statement contains an else branch while a default is active. The else branch of an alt statement is taken if no other branch is applicable. If a default is active at the same time, its branches come after all branches of the alt statement. Hence the default altstep can never be executed if an else branch is present.


Code Example:

.. code-block:: ruby

  testcase myTestcase() runs on MyComponent {
    var default myDefaultVar := activate(myAltstep(t))
    alt {
      [] p.receive(charstring:("foo1")) {
        p.send("ack")
      }
      [] p.receive(charstring:("bar1")) {
        p.send("nack")
      }
      [else] {
        setverdict(fail)
        log("unexpected behavior")
      }
    }
    deactivate(myDefaultVar)
  }

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

