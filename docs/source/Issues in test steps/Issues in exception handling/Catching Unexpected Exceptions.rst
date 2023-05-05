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

References:

 * `JUnit Anti-patterns <https://exubero.com/junit/anti-patterns/>`_

