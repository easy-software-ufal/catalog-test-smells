Doppelgänger
^^^^^
**Definition:**

* In order to test something, you have to copy parts of the code under test into a new class with the same name and package and you have to use classpath magic or a custom classloader to make sure it is visible first (so your copy is picked up). This pattern indicates an unhealthy amount of hidden dependencies which you can't control from a test.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_
