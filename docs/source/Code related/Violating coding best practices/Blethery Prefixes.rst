Blethery Prefixes
^^^^^
**Definition:**

* Where the implementation of a single line of test code is prefixed by a lot of characters before we get to the point


**Code Example:**

.. code-block:: java

    @Test
    void someTest() {
        Mockito.when(someMock.get())
        .thenReturn(123);
    
        ...
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

