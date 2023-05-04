Require External Resources
^^^^^
Definitions:

* Test require external resources but can not guarantee their state and availability


Code Example:

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

References:

 * `A testing anti-pattern safari <https://www.youtube.com/watch?v=VBgySRk0VKY>`_

