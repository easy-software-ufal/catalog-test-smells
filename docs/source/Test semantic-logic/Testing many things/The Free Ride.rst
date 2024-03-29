The Free Ride
^^^^^
**Definition:**

* When an extra assertion is added in an existing test to cover a new scenario case

**Also Known As:**

* Eager Test

**Code Example:**

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

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Smells in software test code: A survey of knowledge in industry and academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_
* `TDD Anti-patterns: The Free Ride / Piggyback <https://matheus.ro/2018/04/30/tdd-antipatterns-the-free-ride-piggyback/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `TDD and anti-patterns - Chapter 5 <https://www.codurance.com/publications/tdd-and-anti-patterns-chapter-5>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Tdd antipatterns: The free ride <https://semaphoreci.com/blog/2014/06/24/tdd-antipatterns-the-free-ride.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Test-Driven Development: TDD Anti-Patterns <https://bryanwilhite.github.io/the-funky-knowledge-base/entry/kb2076072213/>`_
* `Unit Testing Anti-Patterns, Full List <https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html>`_
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_
