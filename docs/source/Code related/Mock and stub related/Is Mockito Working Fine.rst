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


References:

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_

