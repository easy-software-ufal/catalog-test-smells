Oversharing On Setup
^^^^^
Definition:

* Where every test sets up a lot of shared data which only some tests need.


Code Example:

.. code-block:: javascript

  beforeEach(() => {
    databaseConnection = openDatabase();
    inputFile = loadBigFile();
    userList = loadUserList();
    imageData = loadImageBytes();
  });

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

