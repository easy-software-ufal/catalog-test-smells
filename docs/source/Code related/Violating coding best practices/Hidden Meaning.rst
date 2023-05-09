Hidden Meaning
^^^^^
**Definition:**

* Where something that should be part of the execution of the test, and appear in a test report, is hidden in a comment – essentially comment instead of name


**Code Example:**

.. code-block:: java

  @Test
  public void restApi() {
      int response = client.get("/endpoint");
  
      // the status code returned from the get
      // should be OK, indicating
      // the endpoint is healthy
      assertEquals(200, response);
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

