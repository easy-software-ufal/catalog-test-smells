Identity Dodgems
^^^^^
**Definition:**

* where each test case shares some sort of global resource – perhaps a database, or a singleton data store, so needs to choose identifiers carefully in order to avoid collisions with other tests. Better in this case to use a central ID generator, to avoid accidental collisions, or each test having to be aware of all other tests’ choice of IDs.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

