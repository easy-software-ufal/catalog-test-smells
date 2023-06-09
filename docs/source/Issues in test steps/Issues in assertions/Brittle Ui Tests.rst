Brittle Ui Tests
^^^^^
**Definition:**

* Tests having fixed delays, bad selectors and targeting elements, and difficult investigating failures


**Code Example:**

.. code-block:: java

    driver.Url = "http://somedomain/url_that_delays_loading";
    Thread.Sleep(5000);
    IWebElement myDynamicElement = driver.FindElement(By.Id("someDynamicElement"));
    
**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Tips to avoid brittle ui tests <https://code.tutsplus.com/tutorials/tips-to-avoid-brittle-ui-tests--net-35188>`_ :octicon:`file-code;1em` :octicon:`sync;1em`
