Mockito Any() Vs. Isa()
^^^^^
Definitions:

* Misuse of mockito’s matchers classes to type checks


Code Example:

.. code-block:: java

  verify(async).execute(any(AddOrganizationAction.class),
    any(AsyncCallback.class));

  // wrong pass
  verify(async).execute(any(AddPersonToOrganizationAction.class),
    any(AsyncCallback.class));

.. code-block:: java

  verify(async).execute(isA(AddOrganizationAction.class),
    any(AsyncCallback.class));
References:

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_

