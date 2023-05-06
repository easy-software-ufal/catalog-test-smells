Missing Parameterised Test
^^^^^
Definition:

* When you did it the long way round because you didn’t bring in parameterisation


Code Example:

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

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

