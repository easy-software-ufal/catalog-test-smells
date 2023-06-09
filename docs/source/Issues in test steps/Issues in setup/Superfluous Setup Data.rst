Superfluous Setup Data
^^^^^
**Definition:**

* Occurs when testing queries or filters, in which you only expect to get a subset of the data back. The underlying idea is that, in order to be thorough, “extra” data should be present to show that the query or filter works as required.


**Code Example:**

.. code-block:: java

  @Test
  public void givenMultipleWidgetsExistWhenQueriedByNameThenOnlyWidgetAFound() {
  insertDefaultWidget("a");
  insertDefaultWidget("b");
  insertDefaultWidget("c");
  
  WidgetQuery widgetQuery = new WidgetQuery();
  List<Widget> results = widgetQuery.findByName("a");
  
  assertEquals(1, results.size());
  assertEquals("a", results[0].getName());
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Testing anti-patterns <https://medium.com/jameskbride/testing-anti-patterns-b5ffc1612b8b>`_ :octicon:`file-code;1em`
