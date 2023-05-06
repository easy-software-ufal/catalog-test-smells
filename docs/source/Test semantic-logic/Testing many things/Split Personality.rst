Split Personality
^^^^^
Definition:

* A test method that attempts to test several behaviors of the tested object.


Code Example:

.. code-block:: java

    @Test
    public void testCalculatePrice() {
        // Test scenario 1: Calculate price for customer with loyalty discount
        Customer customer = new Customer();
        customer.setLoyaltyPoints(100);
        double price = Product.calculatePrice(customer, 20.0, 10.0);
        assertEquals(18.0, price, 0.0);

        // Test scenario 2: Calculate price for customer without loyalty discount
        Customer customer2 = new Customer();
        customer2.setLoyaltyPoints(0);
        double price2 = Product.calculatePrice(customer2, 20.0, 10.0);
        assertEquals(20.0, price2, 0.0);

        // Test scenario 3: Calculate price for product with no discount
        Customer customer3 = new Customer();
        customer3.setLoyaltyPoints(50);
        double price3 = Product.calculatePrice(customer3, 30.0, 0.0);
        assertEquals(30.0, price3, 0.0);
    }


References:

 * `Developer test anti-patterns by lasse koskela <https://www.youtube.com/watch?v=3Fa69eQ6XgM>`_

