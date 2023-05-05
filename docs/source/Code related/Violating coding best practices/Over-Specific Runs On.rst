Over-Specific Runs On
^^^^^
Definition:

* A behavioral entity (function, test case or altstep) is declared to run on a component, but uses only elements of this component’s super-component or no elements of the component at all.


Code Example:

.. code-block:: pseudo

  type component BaseComponentType {
    port OutPort pOut;
  }

  type component ExtendedComponentType extends BaseComponentType {
    port InPort pIn;
    timer t;
  }

  function f(string aMessage) runs on ExtendedComponentType {
    if (checkSomething()) {
      pOut.sent(aMessage);
    }
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

