Test Tautology
^^^^^
**Definition:**

* Generally speaking one does not want to duplicate the logic between tests and code. So replicating a regexp or something else in the test is not an option.


**Code Example:**

.. code-block:: ruby

  Assertions.assertThat(processTemplate("param1", "param2")).isEqualTo(String.format("this is '%s', and this is '%s'", param1, param2));

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `How to write good tests <https://github.com/mockito/mockito/wiki/How-to-write-good-tests>`_ :octicon:`file-code;1em`

