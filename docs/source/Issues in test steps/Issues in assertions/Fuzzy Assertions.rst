Fuzzy Assertions
^^^^^
Definition:

* Where lack of control for the system under test, causes us not to be able to predict the exact outcome, leading to fuzzy or partial matching in our assertions


Code Example:

.. code-block:: javascript

  readUser = system.retrieveUser(id)
 
  //fuzzy match
  assert(user).matches([
      { obj.firstName == 'John' },
      { obj.lastName == 'Smith' },
      { obj.id instanceof UUID },
      { obj.creationDate - now() < inSeconds(5) }
  ])

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

