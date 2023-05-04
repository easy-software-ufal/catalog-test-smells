The Free Ride
^^^^^
Definitions:

* When an extra assertion is added in an existing test to cover a new scenario case

Also Known As:

* Piggyback

Code Example:

.. code-block:: java

    public void CalculateDiscount_ExpectedDiscountForFirstTimePurchase()
    {
        //Arrange            
        decimal expected = 0.1M;
        decimal expectedResultAge = 0.2M;

        var sut = new DiscountCalculator();

        //Act
        var result = sut.CalculateDiscount(true, 30);
        var resultAge = sut.CalculateDiscount(false, 65);

        //Assert            
        Assert.Equal(expected, result);
        Assert.Equal(expectedResultAge, resultAge);
    }

References:

 * `TDD Anti-patterns: The Free Ride / Piggyback <https://matheus.ro/2018/04/30/tdd-antipatterns-the-free-ride-piggyback/>`_
 * `Tdd antipatterns: The free ride <https://semaphoreci.com/blog/2014/06/24/tdd-antipatterns-the-free-ride.html>`_

