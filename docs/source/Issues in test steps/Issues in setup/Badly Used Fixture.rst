Badly Used Fixture
^^^^^
**Definition:**

* A Badly Used Fixture is a fixture that is not fully used by the tests in the test-suite.


**Code Example:**

.. code-block:: java

    public class ShoppingCartTest {
        private ShoppingCart cart;

        @Before
        public void setUp() {
            cart = new ShoppingCart();
            cart.addItem(new Item("Shirt", 25.0));
            cart.addItem(new Item("Pants", 50.0));
        }

        @Test
        public void testEmptyCart() {
            cart.clear();
            assertTrue(cart.getItems().isEmpty());
        }

        @Test
        public void testAddItem() {
            cart.addItem(new Item("Shoes", 75.0));
            assertEquals(3, cart.getItems().size());
        }

        // This test doesn't need to use the pre-selected items
        @Test
        public void testRemoveItem() {
            cart.removeItem(new Item("Shirt", 25.0));
            assertEquals(1, cart.getItems().size());
        }
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

