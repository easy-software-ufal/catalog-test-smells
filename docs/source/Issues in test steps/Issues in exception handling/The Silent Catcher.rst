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

 * `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_

