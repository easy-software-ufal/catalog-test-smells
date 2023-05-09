Messy Test
^^^^^
Definition:

* Tests that contain repeated code, copy&paste, disorganized structure and literal values


Code Example:

.. code-block:: java

    @Test
    public void testCalculatePrice() {
        // Set up test data
        int quantity = 10;
        String productCode = "A123";
        double pricePerUnit = 1.99;
        double expectedPrice = 19.9;
        
        // Perform the calculation
        double actualPrice = quantity * pricePerUnit;
        
        // Check if the actual price matches the expected price
        if (actualPrice != expectedPrice) {
            fail("Expected price does not match actual price.");
        }
        
        // Perform the same calculation with different input values
        quantity = 5;
        productCode = "B456";
        pricePerUnit = 0.99;
        expectedPrice = 4.95;
        actualPrice = quantity * pricePerUnit;
        if (actualPrice != expectedPrice) {
            fail("Expected price does not match actual price.");
        }
        
        // Perform the same calculation with different input values
        quantity = 20;
        productCode = "C789";
        pricePerUnit = 2.49;
        expectedPrice = 49.8;
        actualPrice = quantity * pricePerUnit;
        if (actualPrice != expectedPrice) {
            fail("Expected price does not match actual price.");
        }
    }


References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `A testing anti-pattern safari <https://www.youtube.com/watch?v=VBgySRk0VKY>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

