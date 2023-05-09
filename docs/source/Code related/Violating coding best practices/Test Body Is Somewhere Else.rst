Test Body Is Somewhere Else
^^^^^
Definition:

* When the test method calls another method entirely with no other implementation in the test method – often a sign of missing parameterised test


Code Example:

.. code-block:: java

  @Test
  public void hasCorrectFoo() {
    checkFoo();
  }
  
  private static checkFoo() {
    Foo foo = service.getFoo();
    assertThat(foo.getBar()).isEqualTo("baz");
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

