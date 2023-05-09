Over Refactoring Of Tests
^^^^^
Definition:

* where you can’t read them because they’ve been DRYed out to death


Code Example:

.. code-block:: javascript

  // Over Refactoring Of Test
  assertThat(calculateAnswer(INPUT))
   .isEqualTo(EXPECTED);

.. code-block:: javascript

  //before
  assertThat(calculateAnswercountTheWordsIn("This is a string"))
   .isEqualTo(4);

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

