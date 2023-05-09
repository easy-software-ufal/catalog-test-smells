Irrelevant Information
^^^^^
Definition:

* The test is exposing a lot of irrelevant details about the fixture that distract the test reader from what really affects the behavior of the SUT.


Code Example:

.. code-block:: java

  public void testAddItemQuantity_severalQuantity_v10(){
      //   Setup Fixture
      Address billingAddress = createAddress( "1222 1st St SW", "Calgary", "Alberta", "T2N 2V2", "Canada");
      Address shippingAddress = createAddress( "1333 1st St SW", "Calgary", "Alberta", "T2N 2V2", "Canada");
      Customer customer = createCustomer( 99, "John", "Doe", new BigDecimal("30"),
                         billingAddress, shippingAddress);
      Product product = createProduct( 88,"SomeWidget",new BigDecimal("19.99"));
      Invoice invoice = createInvoice(customer);
      // Exercise SUT
      invoice.addItemQuantity(product, 5);
      // Verify Outcome
      LineItem expected = new LineItem(invoice, product,5, new BigDecimal("30"), new BigDecimal("69.96"));
      assertContainsExactlyOneLineItem(invoice, expected);
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Detecting Redundant Unit Tests for AspectJ Programs <https://ieeexplore.ieee.org/abstract/document/4021983>`_

