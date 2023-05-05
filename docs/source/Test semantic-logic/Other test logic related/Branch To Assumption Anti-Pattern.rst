Branch To Assumption Anti-Pattern
^^^^^
Definition:

* An assumption is conditionally executed.


Code Example:

.. code-block:: java

  void Test(int i, int j) {
    if (i < 0)
    PexAssume.IsTrue(j > 0);
    ...
  }

References:

 * `Parameterized Test Patterns For Effective Testing with Pex <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.159.6145&rep=rep1&type=pdf>`_

