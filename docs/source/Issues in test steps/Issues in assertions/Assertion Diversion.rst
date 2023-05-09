Assertion Diversion
^^^^^
Definition:

* Where the wrong sort of assert is used, thus making a test failure harder to understand


Code Example:

.. code-block:: java

    Boolean isValid = false;
    if (actualResult.contains("foo")) {
        isValid = true;
    }
    assertEquals(true, isValid)

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

