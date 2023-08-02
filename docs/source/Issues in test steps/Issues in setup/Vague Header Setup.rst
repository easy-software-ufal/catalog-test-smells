Vague Header Setup
^^^^^
**Definition:**

* A vague header setup smell occurs when fields are solely initialized in the header of a class. We consider this a smell as the behavior of the code is not explicitly defined and depends on the field modifier (static or member) as well as on the implementation of the test framework. Vague header setups might hamper code comprehension and maintainability, as fields can be placed anywhere in the class. Further, in many test frameworks exception messages are more expressive for fields initialized in the setup.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Automated Detection of Test Fixture Strategies and Smells <https://ieeexplore.ieee.org/document/6569744>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`comment-discussion;1em`
* `Strategies for avoiding text fixture smells during software evolution <https://ieeexplore.ieee.org/document/6624053>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
