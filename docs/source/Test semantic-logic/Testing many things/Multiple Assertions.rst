Multiple Assertions
^^^^^
Definition:

* When a test method contains multiple assertion statements, it is an indication that the method is testing too much


Code Example:

.. code-block:: java
    
    public class MyTestCase extends TestCase {
        public void testSomething() {
            // Set up for the test, manipulating local variables
            assertTrue(condition1);
            assertTrue(condition2);
            assertTrue(condition3);
        }
    }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `JUnit Anti-patterns <https://exubero.com/junit/anti-patterns/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

