Hard-Coded Test Data
^^^^^
**Definition:**

* Data values in the fixture, assertions or arguments of the SUT are hard-coded in the Test Method obscuring cause-effect relationships between inputs and expected outputs.


**Code Example:**

.. code-block:: java

    public void testAddItemQuantity_severalQuantity_v12(){
        //  Setup Fixture
        Customer cust = createACustomer(new BigDecimal("30"));
        Product prod = createAProduct(new BigDecimal("19.99"));
        Invoice invoice = createInvoice(cust);
        // Exercise SUT
        invoice.addItemQuantity(prod, 5);
        // Verify Outcome
        LineItem expected = new LineItem(invoice, prod, 5,
                new BigDecimal("30"), new BigDecimal("69.96"));
        assertContainsExactlyOneLineItem(invoice, expected);
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Detecting redundant unit tests for AspectJ programs <https://ieeexplore.ieee.org/abstract/document/4021983>`_
* `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
