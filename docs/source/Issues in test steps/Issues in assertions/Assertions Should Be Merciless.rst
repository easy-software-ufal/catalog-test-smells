Assertions Should Be Merciless
^^^^^
**Definition:**

* Tests whose assertions do not prove the test method works correctly


**Code Example:**

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


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
