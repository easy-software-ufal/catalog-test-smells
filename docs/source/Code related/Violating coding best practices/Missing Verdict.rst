Missing Verdict
^^^^^
**Definition:**

* A test case does not set a verdict. Normally a test case should set a verdict before terminating.


**Code Example:**

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


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
* `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

