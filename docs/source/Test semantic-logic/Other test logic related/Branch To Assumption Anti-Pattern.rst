Branch To Assumption Anti-Pattern
^^^^^
**Definition:**

* An assumption is conditionally executed.


**Code Example:**

.. code-block:: java

  void Test(int i, int j) {
    if (i < 0)
    PexAssume.IsTrue(j > 0);
    ...
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Parameterized Test Patterns For Effective Testing with Pex <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.159.6145&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

