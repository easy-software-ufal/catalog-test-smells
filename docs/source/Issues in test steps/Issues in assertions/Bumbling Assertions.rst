Bumbling Assertions
^^^^^
**Definition:**

* Where there was a more articulate assertion available, but we chose a less sophisticated one and kind of got the message across. E.g. testing exceptions the hard way, or using equality check on list size, rather than a list size assertion.


**Code Example:**

.. code-block:: java

  Optional<Foo> result = service.getFoos(123);
  assertNotNull(result);
  assertThat(result).isNotEmpty();
  assertThat(result.getBar()).isNotNull();
  assertThat(result.getBar()).hasSize(1);
  assertThat(result.getBar().get(0)).isEqualTo("buzz");


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`
