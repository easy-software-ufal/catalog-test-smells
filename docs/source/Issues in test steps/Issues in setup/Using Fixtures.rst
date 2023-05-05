Using Fixtures
^^^^^
Definition:

* When a test uses fixtures to prepare and reuse test data.
* It is not clear where the user came from and how it is set up.
* We are testing against a “magic value” — implying something was defined in some code, somewhere else.


Code Example:

.. code-block:: yml

  # spec/fixtures/users.yml
  marko:
    first_name: Marko
    last_name: Anastasov
    phone: 555-123-6788

.. code-block:: ruby

  RSpec.describe User do
    fixtures :all

    describe "#full_name" do
      it "is composed of first and last name" do
        user = users(:marko)
        expect(user.full_name).to eql "Marko Anastasov"
      end
    end
  end

References:

 * `Rails Testing Antipatterns: Fixtures and Factories <https://semaphoreci.com/blog/2014/01/14/rails-testing-antipatterns-fixtures-and-factories.html>`_

