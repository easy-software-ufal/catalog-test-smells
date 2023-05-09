Context Logic In Production Code
^^^^^
Definition:

* When the production code becomes aware of the context in which it is used.


Code Example:

.. code-block:: java

  public static void SaveToDatabase(Customer customerToWrite)
  {
    if (AreWeTesting)
      WriteWithMockDatabase(customerToWrite);
    else
      Write(customerToWrite);
  }

References:

 * `Unit Testing Smells: What Are Your Tests Telling You? <https://dzone.com/articles/unit-testing-smells-what-are-your-tests-telling-yo>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

