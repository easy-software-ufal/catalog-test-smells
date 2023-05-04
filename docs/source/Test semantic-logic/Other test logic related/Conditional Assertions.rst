Conditional Assertions
^^^^^
Definitions:

* it makes your test non-deterministic: you will never be sure which path will be verified in the next pass


Code Example:

.. code-block:: javascript

  if (existsInSystem(testUser)) {
    // test for existing user...
  } else {
    // test for not existing user...
  }

References:

 * `Anti-patterns in test automation <https://www.codementor.io/@mgawinecki/anti-patterns-in-test-automation-101c6vm5jz>`_

