The Ugly Mirror
^^^^^
Definition:

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
 * `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
 * `Java: code duplication in classes and their junit test cases <https://stackoverflow.com/questions/10781050/java-code-duplication-in-classes-and-their-junit-test-cases>`_
 * `Smells in software test code: A survey of knowledge in industry and academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_

