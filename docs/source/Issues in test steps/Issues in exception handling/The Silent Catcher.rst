The Silent Catcher
^^^^^
**Definition:**

* A test that passes if an exception is thrown. Even if the exception that actually occurs is one that is different than the one the developer intended.

**Also Known As:**

* The Secret Catcher

**Code Example:**

.. code-block:: csharp

  [Test]
  [ExpectedException(typeof(Exception))]
  public void ItShouldThrowDivideByZeroException()
  {
    // some code that throws another exception yet passes the test
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Smells in software test code: A survey of knowledge in industry and academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_ :octicon:`file-code;1em`
