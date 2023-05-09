Conditional Assertions
^^^^^
Definition:

* it makes your test non-deterministic: you will never be sure which path will be verified in the next pass


Code Example:

.. code-block:: javascript

  if (existsInSystem(testUser)) {
    // test for existing user...
  } else {
    // test for not existing user...
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Anti-patterns in test automation <https://www.codementor.io/@mgawinecki/anti-patterns-in-test-automation-101c6vm5jz>`_ :octicon:`file-code;1em`
 * `On the Maintenance of System User Interactive Tests <https://orbilu.uni.lu/handle/10993/48254>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `Smells in System User Interactive Tests <https://arxiv.org/abs/2111.02317>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

