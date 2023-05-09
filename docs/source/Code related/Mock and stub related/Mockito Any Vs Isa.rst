Mockito Any() Vs. Isa()
^^^^^
Definition:

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
References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

