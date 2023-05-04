Slow Test
^^^^^
Definitions:

* Slow tests are kind of tests which take long enough to run


Code Example:

.. code-block:: ruby
  
  class SlowTest < Test::Unit::TestCase
    def test_fast
      assert true
    end

    def test_slow
      MyClass.slow_method
      assert true
    end
  end

References:

 * `A testing anti-pattern safari <https://www.youtube.com/watch?v=VBgySRk0VKY>`_

