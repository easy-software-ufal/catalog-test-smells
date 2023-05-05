The Ugly Mirror
^^^^^
Definitions:

* When you occasionally find yourself staring at a spec that looks exactly like the code under test, there’s surprisingly little win left to enjoy.

Code Example:

.. code-block:: ruby

  require "test/unit"

  User = Struct.new(:first_name, :last_name, :email) do
    def to_s
      "#{last_name}, #{first_name} <#{email}>"
    end
  end

  class UserTest < Test::Unit::TestCase
    def test_to_s_includes_name_and_email
      user = User.new("John", "Smith", "jsmith@example.com")
      assert_equal "#{user.last_name}, #{user.first_name} <#{user.email}>", user.to_s
    end
  end


References:

 * `Testing anti-patterns: How to fail with 100% test coverage <https://jasonrudolph.com/blog/testing-anti-patterns-how-to-fail-with-100-test-coverage/>`_
 * `Testing anti-patterns: The ugly mirror <https://jasonrudolph.com/blog/2008/07/30/testing-anti-patterns-the-ugly-mirror/>`_

