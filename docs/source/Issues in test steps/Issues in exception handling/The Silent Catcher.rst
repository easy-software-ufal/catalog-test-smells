The Silent Catcher
^^^^^
Definition:

* A test that passes if an exception is thrown. Even if the exception that actually occurs is one that is different than the one the developer intended.


Code Example:

.. code-block:: csharp

  [Test]
  [ExpectedException(typeof(Exception))]
  public void ItShouldThrowDivideByZeroException()
  {
    // some code that throws another exception yet passes the test
  }

References:

 * `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_ :octicon:`file-code;1em`
 * `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
 * `Smells in Software Test Code: A Survey of Knowledge in Industry and Academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_

