Order Dependent Tests
^^^^^
Definition:

* The tests have to be executed in a certain order due to dependencies between them.


Code Example:

.. code-block:: ruby

  class AnimalTest < Test::Unit::TestCase

    def test_create_record
      a = Animal.create!(name:"Lion")
      assert_not_nil a
    end

    def test_find_record
      a = Animal.find_by_name("Lion")
      assert_not_nil a
    end
    
  end

References:

 * `A testing anti-pattern safari <https://www.youtube.com/watch?v=VBgySRk0VKY>`_
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_
 * `Smells of Testing (signs your tests are bad) <https://jakescruggs.blogspot.com/2009/04/smells-of-testing-signs-your-tests-are.html>`_

