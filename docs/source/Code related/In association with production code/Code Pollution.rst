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
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Code pollution <https://enterprisecraftsmanship.com/posts/code-pollution/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

