Asserting Pre-Condition And Invariants
^^^^^
Definition:

* Using the same API to express pre-conditions (i.e. argument validation), post-conditions, invariants, and assertions.


Code Example:

.. code-block:: csharp

  public void Parse(string input) {
    // pre-condition
    Debug.Assert(input != null, "invalid argument");
    ...
    // invariant
    Debug.Assert(condition, "this should not happen");
  }

References:

 * `Parameterized Test Patterns For Effective Testing with Pex <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.159.6145&rep=rep1&type=pdf>`_

