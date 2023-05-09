Test Tautology
^^^^^
Definition:

* Generally speaking one does not want to duplicate the logic between tests and code. So replicating a regexp or something else in the test is not an option.


Code Example:

.. code-block:: ruby

  Assertions.assertThat(processTemplate("param1", "param2")).isEqualTo(String.format("this is '%s', and this is '%s'", param1, param2));

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `How to write good tests <https://github.com/mockito/mockito/wiki/How-to-write-good-tests>`_ :octicon:`file-code;1em`

