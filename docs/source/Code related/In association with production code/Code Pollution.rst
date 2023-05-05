Code Pollution
^^^^^
Definition:

* It takes place when you introduce additional code to your main code base in order to enable unit testing


Code Example:

.. code-block:: csharp

  public class OrderRepository
  {
      public void Save(Order order)
      {
          /* ... */
      }

      public Order GetById(long id)
      {
          /* ... */
      }
  }

.. code-block:: csharp

  [Fact]
  public void Some_integration_test()
  {
      // Arrange
      var repository = new OrderRepository();
      var service = new OrderService(repository);
      long customerId = 42;

      // Act
      service.DoSomething(customerId);

      // Assert
      IReadOnlyList<Order> orders = repository.GetByCustomerId(customerId); // Code added for the use in this unit test
      /* validate orders */
  }

References:

 * `Code pollution <https://enterprisecraftsmanship.com/posts/code-pollution/>`_

