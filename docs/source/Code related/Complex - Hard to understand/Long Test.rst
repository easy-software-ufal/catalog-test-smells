Long Test
^^^^^
Definition:

* A Long Test is a test that consists of lot of code and statements. Such tests are mostly (but not necessarily) complex and badly document the purpose of the test and the application code. Furthermore they tend to test too much functionality, maybe even getting eager.


Also Known As:

* Obscure Test, Verbose Test, Complex Test


Code Example:

.. code-block:: ruby

  # Subject under test
  class Stack
    def initialize
      @items = []
    end

    def push(item)
      @items << item
    end

    def pop
      @items.pop
    end

    def peek
      @items.last
    end

    def depth
      @items.size
    end
  end

  # Test
  class Long < SmellTest
    def test_make_sure_everything_works
      subject = Stack.new

      # Test Push
      subject.push("A")
      subject.push("B")
      subject.push("C")

      assert_equal "C", subject.pop
      assert_equal "B", subject.pop
      assert_equal "A", subject.pop

      # Test Peek
      subject.push("D")
      subject.push("E")

      assert_equal "E", subject.peek

      subject.pop

      assert_equal "D", subject.peek

      subject.pop

      # Test Depth
      subject.push("F")
      subject.push("G")

      assert_equal 2, subject.depth

      # Test Pop
      subject.pop
      subject.pop

      assert_equal 0, subject.depth
      assert_equal nil, subject.pop
    end
  end

References:

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
 * `Rule-Based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_

