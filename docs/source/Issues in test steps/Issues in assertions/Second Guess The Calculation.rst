Second Guess The Calculation
^^^^^
Definition:

* Where rather than using concrete test data, we use something that needs us to calculate the correct answer ahead of assertion


Code Example:

.. code-block:: java

    @Test
    public void testCalculatePrice() {
        Order order = new Order();
        order.addProduct(new Product("Product A", 10.0, 2));
        order.addProduct(new Product("Product B", 5.0, 3));
        
        double expectedPrice = 10.0 * 2 + 5.0 * 3;
        double actualPrice = order.calculatePrice();
        
        assertEquals(expectedPrice, actualPrice, 0.001);
    }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

