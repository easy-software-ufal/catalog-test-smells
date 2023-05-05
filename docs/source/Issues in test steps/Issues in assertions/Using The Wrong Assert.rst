Using The Wrong Assert
^^^^^
Definition:

* There are a large number of different methods beginning with assert defined in the Assert class. Each of these methods has slightly different arguments and semantics about what they are asserting. However, many programmers seem to stick with a single assertion method: assertTrue, and then force the argument of this method into the required boolean expression.


Code Example:

.. code-block:: javascript

  assertTrue("Objects must be the same", expected == actual);
  assertTrue("Objects must be equal", expected.equals(actual));
  assertTrue("Object must be null", actual == null);
  assertTrue("Object must not be null", actual != null);

References:

 * `JUnit Anti-patterns <https://exubero.com/junit/anti-patterns/>`_

