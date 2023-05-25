Require External Resources
^^^^^
**Definition:**

* Test require external resources but can not guarantee their state and availability


**Code Example:**

.. code-block:: ruby

  class Clever
    def districts
      url = "/districts"
      key = "DEMO_KEY"
      `curl -u #{key}: #{host}#{url}`
    end
  end

  class External < Test::Unit::TestCase
    def test_get_clever_data
      c = Clever.new
      assert_include c.districts, 'Demo'
    end
  end

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A testing anti-pattern safari <https://www.youtube.com/watch?v=VBgySRk0VKY>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
