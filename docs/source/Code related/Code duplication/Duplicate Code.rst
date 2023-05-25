Duplicate Code
^^^^^
**Definition:**

* For test automation, it's especially easy to find yourself with the same code over and over. Steps such as logging in and navigating through common areas of the application are naturally a part of most scenarios.  However, repeating this same logic multiple times in various places is a code smell. Should there be a change in the application within this flow, you'll have to hunt down all the places where this logic is duplicated within your test code and update each one. This takes too much development time and also poses the risk of you missing a spot, therefore introducing a bug in your test code.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Writing good gherkin <https://techbeacon.com/app-dev-testing/7-ways-tidy-your-test-code>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
