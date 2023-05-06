Self-Test
^^^^^
Definition:

* Tests that do not compare a result with an expected value, but with the result itself


Code Example:

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

References:

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_

