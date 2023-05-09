Multiple Assertions
^^^^^
**Definition:**

* When a test method contains multiple assertion statements, it is an indication that the method is testing too much


**Code Example:**

.. code-block:: java
    
    public class MyTestCase extends TestCase {
        public void testSomething() {
            // Set up for the test, manipulating local variables
            assertTrue(condition1);
            assertTrue(condition2);
            assertTrue(condition3);
        }
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `JUnit Anti-patterns <https://exubero.com/junit/anti-patterns/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

