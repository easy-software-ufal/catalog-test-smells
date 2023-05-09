Generative
^^^^^
Definition:

* A test loops over a data structure of discrete inputs and expected outputs to generate test cases.


Code Example:

.. code-block:: ruby

  # Subject under test
  def to_arabic(roman)
    roman.chars.each_with_index.map { |x, i|
      next_x = roman[i + 1]
      if x == "I"
        ["V", "X"].include?(next_x) ? -1 : 1
      elsif x == "V"
        next_x == "X" ? -5 : 5
      elsif x == "X"
        next_x == "C" ? -10 : 10
      end
    }.reduce(:+)
  end

  # Test
  class Generative < SmellTest
    EXAMPLES = {
      "I" => 1,
      "II" => 2,
      "III" => 3,
      "IV" => 4,
      "V" => 5,
      "VI" => 6,
      "VII" => 7,
      "VIII" => 8,
      "IX" => 9,
      "X" => 10
    }.each do |(roman, arabic)|
      define_method "test_roman_#{roman}_is_#{arabic}" do
        result = to_arabic(roman)

        assert_equal result, arabic
      end
    end
  end

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

