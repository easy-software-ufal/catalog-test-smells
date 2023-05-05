Tangential
^^^^^
Definition:

* The subject and its test claim to be focused on something, but the bulk of their complexity is focused on a different (often subordinate) responsibility.


Code Example:

.. code-block:: ruby

  class Tangential < SmellTest
    def test_no_type
      user = OpenStruct.new

      set_attr(user, :name, "Fred")

      assert_equal "Fred", user.name
    end

    def test_string_type_correct
      user = OpenStruct.new

      set_attr(user, :name, "Frida", :string)

      assert_equal "Frida", user.name
    end

    def test_string_type_incorrect
      user = OpenStruct.new

      error = assert_raises {
        set_attr(user, :age, 42, :string)
      }
      assert_equal "42 is not a string", error.message
    end

    def test_phone_type_correct
      user = OpenStruct.new

      set_attr(user, :mobile, "(614) 349-4279", :phone)

      assert_equal "(614) 349-4279", user.mobile
    end

    def test_phone_type_incorrect
      user = OpenStruct.new

      error = assert_raises {
        set_attr(user, :mobile, "1337", :phone)
      }
      assert_equal "1337 is not a phone", error.message
    end

    def test_invalid_first_phone_character_cannot_start_with_1
      user = OpenStruct.new

      assert_raises {
        set_attr(user, :mobile, "(123) 456-7890", :phone)
      }
    end

    def test_simple_japanese_phone_number
      user = OpenStruct.new

      set_attr(user, :mobile, "090-1790-1357", :phone)

      assert_equal "090-1790-1357", user.mobile
    end

    def test_japanese_without_the_trunk
      user = OpenStruct.new

      assert_raises {
        set_attr(user, :mobile, "90-1790-1357", :phone)
      }
    end

    def test_international_japanese_phone_number
      user = OpenStruct.new

      set_attr(user, :mobile, "011-81-90-1790-1357", :phone)

      assert_equal "011-81-90-1790-1357", user.mobile
    end
  end

References:

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_

