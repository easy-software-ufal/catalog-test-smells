Improper Clean Up After Tests Have Been Run
^^^^^
**Definition:**

* Improper cleanup occurs when the code that cleans up the mocks and anything created in the test is insufficient or entirely lacking. It may leave files open or objects in memory causing memory leaks. This can be especially important if your tests are doing any type of file manipulation or you are creating files specifically for testing.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

 * `Anti-Patterns In Unit Testing <https://completedeveloperpodcast.com/anti-patterns-in-unit-testing/>`_

