Over Exertion Assertion
^^^^^
**Definition:**

* Where the implementation of an assertion is heavy and in the body of the test, rather than in an assertion library


**Code Example:**

.. code-block:: java

  List results = service.getFoosInOrder();
 
  int previousOrder = results.get(0).getOrdering();
  for(int i=0; i= because they can sometimes be of same value
    if (!(ordering>=previousOrder)) {
      Assert.fail("Not in ascending order");
    }
    previousOrder = ordering;
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

