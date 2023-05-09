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

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

