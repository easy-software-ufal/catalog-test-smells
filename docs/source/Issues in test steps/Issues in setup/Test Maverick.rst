Test Maverick
^^^^^
**Definition:**

* A test method is a maverick when the class comprising the test method contains an implicit setup, but the test method is completely independent from the implicit setup procedure. The setup procedure will be executed before the test method is executed, but it is not needed. Also, understanding the effect-cause relationship between setup and test method can be hampered. Discovering that test methods are unrelated from the implicit setup can be time consuming.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Automated Detection of Test Fixture Strategies and Smells <https://ieeexplore.ieee.org/document/6569744>`_ :octicon:`comment-discussion;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Strategies for avoiding text fixture smells during software evolution <https://ieeexplore.ieee.org/document/6624053>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_

