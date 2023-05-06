Brittle Ui Tests
^^^^^
Definition:

* Tests having fixed delays, bad selectors and targeting elements, and difficult investigating failures


Code Example:

.. code-block:: java

    driver.Url = "http://somedomain/url_that_delays_loading";
    Thread.Sleep(5000);
    IWebElement myDynamicElement = driver.FindElement(By.Id("someDynamicElement"));
    
References:

 * `Tips to avoid brittle ui tests <https://code.tutsplus.com/tutorials/tips-to-avoid-brittle-ui-tests--net-35188>`_

