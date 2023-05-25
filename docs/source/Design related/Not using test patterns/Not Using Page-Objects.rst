Not Using Page-Objects
^^^^^
**Definition:**

* Page objects are just a design pattern to ensure automated UI tests use reusable, modular code. Not using them, eg, writing WebDriver code directly in step definitions, means any changes to your UI will require updates in lots of different places instead of the one ‘page’ class.


**Code Example:**

.. code-block:: csharp

  [When(@'I buy some '(.*)' tea')]
  public void WhenIBuySomeTea(string typeOfTea)
  {
    Driver.FindElement(By.Id('tea-'+typeOfTea)).Click();
    Driver.FindElement(By.Id('buy')).Click();
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Five automated acceptance test anti-patterns <https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_ :octicon:`file-code;1em`
