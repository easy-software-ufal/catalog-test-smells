The Dead Tree
^^^^^
**Definition:**

* A test which where a stub was created, but the test wasn't actually written.

**Also Known As:**

* Process Compliance Backdoor

**Code Example:**

.. code-block:: typescript

  class TD_SomeClass {
    public void testAdd() {
      assertEquals(1+1, 2);
    }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_ :octicon:`file-code;1em`
