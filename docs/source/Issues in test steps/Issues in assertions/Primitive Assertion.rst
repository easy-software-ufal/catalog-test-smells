Primitive Assertion
^^^^^
**Definition:**

* Assertions that use primitive content to express intent


**Code Example:**

.. code-block:: java

    @Test
    public void testMethod() {
        MyClass obj = new MyClass();
        int expected = 5;
        int actual = obj.doSomething();
        assertThat("Result of doSomething() should be greater than expected",
                actual, greaterThan(expected));
    }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Developer test anti-patterns by lasse koskela <https://www.youtube.com/watch?v=3Fa69eQ6XgM>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
