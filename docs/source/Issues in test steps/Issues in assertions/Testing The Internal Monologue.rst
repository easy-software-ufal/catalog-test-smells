Testing The Internal Monologue
^^^^^
**Definition:**

* Where the writer of the test has been so focused on the lines of code in their implementation that they haven’t sought ways to observe the behaviour of the system from the outside.


**Code Example:**

.. code-block:: java

  @Spy
  private Service service = new Service( ... );
  
  @Test
  public void withInputAItDoesTheThing() {
      service.process("A");
      verify(service).internalCall();
  }
  
  @Test
  public void withInputBItDoesntDoTheThing() {
      service.process("B");
      verify(service, never()).internalCall();
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`
