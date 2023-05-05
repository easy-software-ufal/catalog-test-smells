Over-Specific Runs On
^^^^^
Definitions:

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

