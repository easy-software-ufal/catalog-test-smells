Autogeneration
^^^^^
**Definition:**

* Auto-generated tests that test methods instead of behavior


**Code Example:**

.. code-block:: java

  public void testSetGetTimestamp() throws Exception {
    // JUnitDoclet begin method setTimestamp getTimestamp
    java.util.Calendar[] tests = {new GregorianCalendar(), null};

    for (int i = 0; i < tests.length; i++) {
      adapter.setTimestamp(tests[i]);
      assertEquals(tests[i], adapter.getTimestamp());
    }
    // JUnitDoclet end method setTimestamp getTimestamp
  }
  public void testSetGetParam() throws Exception {
    // JUnitDoclet begin method setParam getParam
    String[] tests = {"a", "aaa", "---", "23121313", "", null};
    
    for (int i = 0; i < tests.length; i++) {
      adapter.setParam(tests[i]);
      assertEquals(tests[i], adapter.getParam());
    }
    // JUnitDoclet end method setParam getParam
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
