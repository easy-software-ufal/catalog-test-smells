Test Setup Is Somewhere Else
^^^^^
Definition:


* Where the test method just does the assertions, not the given/when part; this can be acceptable in the case of several tests on a single shared expensive resource setup, but seldom is at other times.

Code Example:

.. code-block:: java

  @Test
  void theOperationIsSuccessful() {
      assertTrue(service.isLastOperationSuccessful());
  }

References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

