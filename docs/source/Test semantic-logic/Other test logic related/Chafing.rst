Chafing
^^^^^
Definition:

* A test in which the author attempts to eliminate as much textual duplication as possible, even if the indirection it introduces confuses future readers of the intention and behavior of the test.


Code Example:

.. code-block:: ruby

  # Subject under test
  def pricing_for_code(code)
    first_factor = 0
    first_factor = 65 if code[0] == 'A'
    first_factor = 55 if code[0] == '7'
    first_factor = 40 if code[0] == '('

    second_factor = 0
    second_factor = 21 if code.size == 3
    second_factor = 19 if code.size == 5
    second_factor = 16 if code.size == 8

    return first_factor * second_factor
  end

  # Test
  require_relative "../../../support/ruby/generate_code"

  class Chafing < SmellTest
    def test_code_one_is_correct
      code = GenerateCode.one()

      result = pricing_for_code(code)

      assert_code_pricing code, result
    end

    def test_code_two_is_correct
      code = GenerateCode.two()

      result = pricing_for_code(code)

      assert_code_pricing code, result
    end

    def test_code_three_is_correct
      code = GenerateCode.three()

      result = pricing_for_code(code)

      assert_code_pricing code, result
    end
  end


References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

