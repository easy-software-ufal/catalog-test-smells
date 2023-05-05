Factories With Random Data Instead Of Sequences
^^^^^
Definition:

* When used alongside factories, random data generators may compromise the reliability of a test suite.


Code Example:

.. code-block:: ruby

  #Random factory

  FactoryBot.define do
    factory :category do
      name { Faker::Lorem.word.capitalize }
    end
  end

.. code-block:: ruby

  #Sequence factory

  FactoryBot.define do
    factory :category do
      sequence(:name) { |n| "Category number #{n}" }
    end
  end


References:

 * `Rails Testing Antipatterns: Fixtures and Factories <https://semaphoreci.com/blog/2014/01/14/rails-testing-antipatterns-fixtures-and-factories.html>`_

