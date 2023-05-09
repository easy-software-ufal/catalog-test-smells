Is Mockito Working Fine?
^^^^^
Definition:

* When the mock framerwork is tested intead of the SUT


Code Example:

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


References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

