Expected Exceptions And Verification
^^^^^
Definition:

* A verification happens after an expected exception is thrown and halts the test method execution


Code Example:


.. code-block:: java

  @Test(expected = RuntimeException.class)
  public void shouldSaveFailureInformationWhenExceptionOccurWhenAddingDomain() {
    //given
    doThrow(new RuntimeException()).when(dnsService)
      .addDomainIfMissing(DOMAIN_ADDRESS);
      
    //when
    domainRegistrator.registerDomain(domain);

    //then
    verify(domainService)
      .saveDomain(domain, false, DNS_FAILURES + 1);
  }


References:

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_

