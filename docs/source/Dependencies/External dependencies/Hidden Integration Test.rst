Hidden Integration Test
^^^^^
Definition:

* A PUT outcome depends on the state of the environment.


Code Example:

.. code-block:: csharp

  [PexMethod]
  void FileExists(string fileName) {
  if (!File.Exists(fileName))
  throw new FileNotFoundException();
  ...
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Parameterized Test Patterns For Effective Testing with Pex <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.159.6145&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

