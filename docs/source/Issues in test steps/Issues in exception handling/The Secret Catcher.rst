The Secret Catcher
^^^^^
**Definition:**

* A test that at first glance appears to be doing no testing, due to absence of assertions. But "The devil is in the details".. the test is really relying on an exception to be thrown and expecting the testing framework to capture the exception and report it to the user as a failure.


Also Known As:

* The Silent Catcher


**Code Example:**

.. code-block:: csharp

  [Test]
  public void ShouldNotThrow()
  {
    DoSomethingThatShouldNotThrowAnException();
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_ :octicon:`file-code;1em`
* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Test-Driven Development: TDD Anti-Patterns <https://bryanwilhite.github.io/the-funky-knowledge-base/entry/kb2076072213/>`_
* `Unit Testing Anti-Patterns, Full List <https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html>`_

