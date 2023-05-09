Is There Anybody There?
^^^^^
**Definition:**

* Any flickering test that occasionally breaks a build – bad test or bad code?


**Code Example:**

.. code-block:: java

    @Test
    public void testMethod() {
        int expected = 5;
        int actual = MyUnstableClass.doSomethingWithRandomReturns();
        assertEquals(expected, actual);
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

