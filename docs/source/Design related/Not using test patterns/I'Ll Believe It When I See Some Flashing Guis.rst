I'Ll Believe It When I See Some Flashing Guis
^^^^^
**Definition:**

* An unhealthy fixation/obsession with testing the app via its GUI 'just like a real user'. Testing business rules through the GUI is a terrible form of coupling. If you write thousands of tests through the GUI, and then change your GUI, thousands of tests break. Rather, test only GUI things through the GUI, and couple the GUI to a dummy system instead of the real system, when you run those tests. Test business rules through an API that doesn't involve the GUI.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_
