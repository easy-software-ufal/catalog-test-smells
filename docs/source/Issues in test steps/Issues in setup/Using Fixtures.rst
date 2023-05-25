Using Fixtures
^^^^^
**Definition:**

* When a test uses fixtures to prepare and reuse test data.


**Code Example:**

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

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Rails Testing Antipatterns: Fixtures and Factories <https://semaphoreci.com/blog/2014/01/14/rails-testing-antipatterns-fixtures-and-factories.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
