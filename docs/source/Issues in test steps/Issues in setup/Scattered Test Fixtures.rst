Scattered Test Fixtures
^^^^^
**Definition:**

* Test fixtures are defined in test cases to set up the environment for test execution. A base test case may define a general test fixture (i.e., a method annotated by @BeforeClass or @Before). When a child test case inherits a base test case, the child test case may define its own test fixture, but may also call the test fixture of the base test case. In multi-level inheritance, when each child test case has its own test fixture, the test fixture code becomes scattered and difficult to maintain.

**Code Example:**

* No code examples yet...
.. TODO CODE EXAMPLE

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Revisiting Test Impact Analysis in Continuous Testing From the Perspective of Code Dependencies <https://ieeexplore.ieee.org/document/9303402/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`

