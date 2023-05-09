Incidental Coverage
^^^^^
**Definition:**

* Is it enough to know that your test suite encounters every line of code? Or don’t you want to be sure that it exercises every line? If you simply encounter the line without asserting that it produces the correct results, are you any better off?


**Code Example:**

.. code-block:: ruby

  require File.dirname(__FILE__) + '/../test_helper'

  class ProductsControllerTest < ActionController::TestCase
    def test_should_get_index
      get :index
    end

    # ... remaining tests omitted
  end

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Testing anti-patterns: How to fail with 100% test coverage <https://jasonrudolph.com/blog/testing-anti-patterns-how-to-fail-with-100-test-coverage/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

