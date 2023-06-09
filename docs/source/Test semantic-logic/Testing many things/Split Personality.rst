Split Personality
^^^^^
**Definition:**

* A test method that attempts to test several behaviors of the tested object.

**Also Known As:**

* Eager Test

**Code Example:**

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


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Developer test anti-patterns by lasse koskela <https://www.youtube.com/watch?v=3Fa69eQ6XgM>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
