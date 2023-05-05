Not Using Page-Objects
^^^^^
Definition:

* Page objects are just a design pattern to ensure automated UI tests use reusable, modular code. Not using them, eg, writing WebDriver code directly in step definitions, means any changes to your UI will require updates in lots of different places instead of the one ‘page’ class.


Code Example:

.. code-block:: csharp

  [When(@&quot;I buy some '(.*)' tea&quot;)]
  public void WhenIBuySomeTea(string typeOfTea)
  {
    Driver.FindElement(By.Id(&quot;tea-&quot;+typeOfTea)).Click();
    Driver.FindElement(By.Id(&quot;buy&quot;)).Click();
  }

References:

 * `Five automated acceptance test anti-patterns <https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_

t-anti-patterns//>`_

