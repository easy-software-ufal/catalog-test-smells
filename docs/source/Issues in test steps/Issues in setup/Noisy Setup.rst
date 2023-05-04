Noisy Setup
^^^^^
Definitions:

* When a verbose sequence of low-level records that is difficult to comprehend is displayed in the setup


Code Example:

.. code-block:: ruby

    let(:product_1) { create(:product, name: 'iPad') }
    let(:product_sale_1) { create(:product_sale, retail_price: 500, product: product_1) }
    let(:product_2) { create(:product, name: 'iPhone') }
    let(:product_sale_2) { create(:product_sale, retail_price: 500, product: product_2) }
    let(:product_sales) { [product_sale_1, product_sale_2] }
    let(:sale) { create(:sale, name: 'Apple Bundle', product_sales: product_sales) }
    let(:user) { create(:user, name: 'Thiago') }
    let!(:line_item) { create(:order_line_item, order: order, sale: sale) }
    let(:order) { create(:order, user: user) }

    it 'retrieves the expected data' do
    # Run the query and make assertions
    end
    
References:

 * `Rails Testing Antipatterns: Fixtures and Factories <https://semaphoreci.com/blog/2014/01/14/rails-testing-antipatterns-fixtures-and-factories.html>`_

