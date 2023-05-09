Catching Unexpected Exceptions
^^^^^
Definition:

* When writing production code, developers are generally aware of the problems of uncaught exceptions, and so are relatively diligent about catching exceptions and logging the problem. In the case of unit tests, however, this pattern is completly wrong!


Code Example:

.. code-block:: java

  public void testCalculation() {
    try {
        deepThought.calculate();
        assertEquals("Calculation wrong", 42, deepThought.getResult());
    }
    catch(CalculationException ex) {
        Log.error("Calculation caused exception", ex);
    }
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `JUnit Anti-patterns <https://exubero.com/junit/anti-patterns/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`

