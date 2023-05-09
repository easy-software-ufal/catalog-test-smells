Missing Parameterised Test
^^^^^
**Definition:**

* When you did it the long way round because you didn’t bring in parameterisation


**Code Example:**

.. code-block:: java

    @ParameterizedTest
    @CsvSource({
    "a,A",
    "b,B",
    "bbb,BBB",
    "bBbB,BBBB"
    })
    void capitalizerTurnsInputToCapitals(String input, String expected) {
        assertThat(Capitalizer.toCapitals(input))
            .isEqualTo(expected);
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

