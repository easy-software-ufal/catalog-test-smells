Assertions Should Be Merciless
^^^^^
Definition:

* Tests whose assertions do not prove the test method works correctly


Code Example:

.. code-block:: java

  @Test
  public void shouldRemoveEmailsByState() {
    //given
    Email pending = createAndSaveEmail("pending","content pending",
    "abc@def.com", Email.PENDING);
    Email failed = createAndSaveEmail("failed","content failed",
    "abc@def.com", Email.FAILED);
    Email sent = createAndSaveEmail("sent","content sent",
    "abc@def.com", Email.SENT);
    //when
    emailDAO.removeByState(Email.FAILED);
    //then
    assertThat(emailDAO.findAll()).doesNotContain(failed);
  }


References:

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_

