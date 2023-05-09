Overspecification
^^^^^
Definition:

* Tests increasingly serve multiple roles in today’s projects. They help us design APIs through test-driven development. They provide confidence that new changes aren’t breaking existing functionality. They offer an executable specification of the application. But can we ever get to a point where we have too much testing?


Code Example:

.. code-block:: ruby

  require File.dirname(__FILE__) + '/../test_helper'

  class ProductsControllerTest < ActionController::TestCase
    def test_something
      product = Product.create(:name => "Frisbee", :price => 5.00)
      get :show, :id => product.id
      assert_response :success
      product = assigns(:product)
      assert_not_nil product
      assert product.valid?
      assert product.name == "Frisbee"
      assert product.price == 5.00
    end
  end


References:

 * `Testing anti-patterns: How to fail with 100% test coverage <https://jasonrudolph.com/blog/testing-anti-patterns-how-to-fail-with-100-test-coverage/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

