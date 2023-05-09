Indecent Exposure
^^^^^
**Definition:**

* Classes and methods should not expose their internals unless there's a good reason to do so. In test automation code bases, we explicitly separate our tests from our framework. It's important to stay true to this by hiding internal framework code from our test layer. It's a code smell to expose class fields such as web elements used in Page Object classes, or class methods that return web elements. Doing so enables test code to access these DOM-specific items, which is not its responsibility.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Writing good gherkin <https://techbeacon.com/app-dev-testing/7-ways-tidy-your-test-code>`_ :octicon:`comment-discussion;1em`

