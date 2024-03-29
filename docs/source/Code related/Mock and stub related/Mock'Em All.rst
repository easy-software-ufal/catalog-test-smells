Mock'Em All
^^^^^
**Definition:**

* When a test overuse all kinds of test double, even when it is not really the best option


**Code Example:**

.. code-block:: java

  @Test
  public void shouldAddTimeZoneToModelAndView() {
    //given
    Context context = mock(Context.class);
    ModelAndView modelAndView = mock(ModelAndView.class);
    given(context.getTimezone()).willReturn("timezone X");
    //when
    new UserDataInterceptor(context)
    .postHandle(null, null, null, modelAndView);
    //then
    verify(modelAndView).addObject("timezone", "timezone X");
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
