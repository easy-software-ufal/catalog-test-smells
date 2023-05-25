Catching Unexpected Exceptions
^^^^^
**Definition:**

* When writing production code, developers are generally aware of the problems of uncaught exceptions, and so are relatively diligent about catching exceptions and logging the problem. In the case of unit tests, however, this pattern is completly wrong!


**Code Example:**

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

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `JUnit Anti-patterns <https://exubero.com/junit/anti-patterns/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
