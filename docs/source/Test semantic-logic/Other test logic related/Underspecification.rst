Underspecification
^^^^^
Definition:

* While it’s clearly possible for a test suite to do too much, it’s far more common for it to do too little.



Code Example:

.. code-block:: ruby

    MIN_FREE_SHIPPING_PRICE = 25.0

    def free_shipping?(total_order_price)
    total_order_price > MIN_FREE_SHIPPING_PRICE
    end

.. code-block:: ruby
    
    def test_free_shipping_returns_true_for_order_above_min_price
    assert free_shipping?(MIN_FREE_SHIPPING_PRICE + 1)
    end

    def test_free_shipping_returns_false_for_order_below_min_price
    assert !free_shipping?(MIN_FREE_SHIPPING_PRICE - 1)
    end

References:

 * `Testing anti-patterns: How to fail with 100% test coverage <https://jasonrudolph.com/blog/testing-anti-patterns-how-to-fail-with-100-test-coverage/>`_

