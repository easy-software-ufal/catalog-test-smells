No Assertions
^^^^^
**Definition:**

* Tests that have no assertions and require the manual verification of log outputs


**Also Known As:**

* Assertionless Test


**Code Example:**

.. code-block:: java

  IResult result = format.execute();
  System.out.println(result.size());
  Iterator iter = result.iterator();
  
  while (iter.hasNext()) {
    IResult r = (IResult) iter.next();
    System.out.println(r.getMessage());
  }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Smells of Testing (signs your tests are bad) <https://jakescruggs.blogspot.com/2009/04/smells-of-testing-signs-your-tests-are.html>`_ :octicon:`sync;1em`
