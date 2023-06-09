Split Logic
^^^^^
**Definition:**

* When the test logic is split into several test objects and their specific assertions


**Code Example:**

.. code-block:: java

    public class AddToCartTests {
        @Test
        public void testAddToCart() {
            // Test adding product to cart
        }
        
        @Test
        public void testCartIsEmptyAfterCheckout() {
            // Checkout process
            // Assert that cart is empty
        }
    }

    public class CheckoutTests {
        @Test
        public void testCheckout() {
            // Checkout process
        }
    }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Developer test anti-patterns by lasse koskela <https://www.youtube.com/watch?v=3Fa69eQ6XgM>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
