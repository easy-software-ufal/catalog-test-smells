Is Mockito Working Fine?
^^^^^
**Definition:**

* When the mock framerwork is tested intead of the SUT


**Code Example:**

.. code-block:: java

  @Test
  public void testFormUpdate() {
    // given
    Form f = Mockito.mock(Form.class);
    Mockito.when(f.isUpdateAllowed()).thenReturn(true);
    // when
    boolean result = f.isUpdateAllowed();
    // then
    assertTrue(result);
  }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

