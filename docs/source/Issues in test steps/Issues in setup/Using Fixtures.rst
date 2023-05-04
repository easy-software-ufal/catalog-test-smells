Using Fixtures
^^^^^
Definitions:

* When a test uses fixtures to prepare and reuse test data on Rails


Code Example:

.. code-block:: ruby

    # spec/fixtures/users.yml
    marko:
    first_name: Marko
    last_name: Anastasov
    phone: 555-123-6788

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

