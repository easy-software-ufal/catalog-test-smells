Long Class
^^^^^
**Definition:**

* To properly execute your automated test, your code must open your application in a browser, perform the necessary actions on the application, and then verify the resulting state of the application. While these are all needed for your test, these are different responsibilities, and having all of these responsibilities together within a single class is a code smell. This smell makes it difficult to grasp the entirety of what's contained within the class, which can lead to redundancy and maintenance challenges.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Writing good gherkin <https://techbeacon.com/app-dev-testing/7-ways-tidy-your-test-code>`_ :octicon:`comment-discussion;1em`

