Multiple Points Of Failure
^^^^^
**Definition:**

* Adding assertions within your framework code is a code smell. It is not this code's responsibility to determine the fate of a test. By doing so, it limits the reusability of the framework code for both negative and positive scenarios.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Writing good gherkin <https://techbeacon.com/app-dev-testing/7-ways-tidy-your-test-code>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
