Self-Test
^^^^^
**Definition:**

* Tests that do not compare a result with an expected value, but with the result itself


**Code Example:**

.. code-block:: java

  @Test
  public void shouldGetMethodsForPoland() {
    //given
    List<PaymentMethod> all = Lists.newArrayList(PaymentMethod.values());
    List<PaymentMethod> methodsAvailableInPoland = Lists.newArrayList();

    for (PaymentMethod method : all) {
      if (method.isEligibleForCountry("PL")) {
        methodsAvailableInPoland.add(method);
      }
    }

    //when
    List<PaymentMethod> methodsForCountry = PaymentMethod
      .getMethodsForCountry("PL", all);
      
    //then
    assertThat(methodsForCountry).isEqualTo(methodsAvailableInPoland);
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

