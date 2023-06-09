Invisible Assertions
^^^^^
**Definition:**

* A test which lacks any explicit assertions, leading future readers in the potentially frustrating position of puzzling over the intention of the test.


**Code Example:**

.. code-block:: ruby

  require "helper"

  # Subject under test
  def is_21?(person)
    if person.age < 21
      raise "Sorry, adults only!"
    end
  end

  # Test
  class InvisibleAssertions < SmellTest
    def test_is_21
      person = OpenStruct.new(age: 21)

      is_21?(person)
    end

    def test_is_under_age
      person = OpenStruct.new(age: 20)

      assert_raises { is_21?(person) }
    end
  end

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
