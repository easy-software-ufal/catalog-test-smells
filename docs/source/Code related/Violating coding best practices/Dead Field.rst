Dead Field
^^^^^
**Definition:**

* Occurs when a class or its super classes have fields that are never used by any test method. Often dead fields are inherited. This can indicate a non-optimal inheritance structure, or that the super class conflicts with the single responsibility principle. Also, dead fields within the test class itself can indicate incomplete or deprecated development activities.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Automated Detection of Test Fixture Strategies and Smells <https://ieeexplore.ieee.org/document/6569744>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Strategies for avoiding text fixture smells during software evolution <https://ieeexplore.ieee.org/document/6624053>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
