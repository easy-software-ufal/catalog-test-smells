Fantasy Tests
^^^^^
Definition:

* Passing tests of code that wouldn't actually work in production, usually as a result of a stub returning a response that's substantially different from how a real instance would behave.


Code Example:

.. code-block:: ruby

  # Subject under test
  class Authorizer
    def initialize(authenticator)
      @authenticator = authenticator
    end

    def roles(user, password)
      if @authenticator.login(user: user, password: password)
        ["admin", "developer", "manager"]
      else
        []
      end
    end
  end

  # Test
  class Fantasy < SmellTest
    def setup
      @authenticator = Minitest::Mock.new(Authenticator.new)
      @subject = Authorizer.new(@authenticator)
      super
    end

    def test_all_roles_if_authenticated
      @authenticator.expect(:login, true, [{user: "hi", password: "bye"}])

      result = @subject.roles("hi", "bye")

      assert_equal ["admin", "developer", "manager"], result
    end

    def test_no_roles_if_not_authenticated
      @authenticator.expect(:login, false, [{user: "hi", password: "no!"}])

      result = @subject.roles("hi", "no!")

      assert_equal [], result
    end
  end

  # Fake production implementations to simplify example test of subject
  class Authenticator
    def login(credentials)
      if !credentials[:password] || !credentials[:"2fa"]
        raise "Both password and two-factor auth token are now required!"
      end
      return true
    end
  end

References:

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_

