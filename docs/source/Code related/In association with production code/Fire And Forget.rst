Fire And Forget
^^^^^
Definitions:

* A test that's at risk of exiting prematurely, typically before its assertions can run and fail the test run if necessary


Code Example:

.. code-block:: ruby

    # Subject under test
    def load_user(id)
    path = "/users/#{id}"

    get(path) { |er, user|
        user.resolved_via = path
        yield er, user if block_given?
    }
    end

    # Test
    class FireAndForget < SmellTest
    include UnreliableMinitestPlugin

    def test_gets_user_and_decorates_path
        load_user(42) { |er, user|
        assert_equal "/users/42", user.resolved_via
        assert_equal "Jo", user.name
        }
    end
    end

    # Fake production implementations to simplify example test of subject
    def get(path)
    Thread.new do
        sleep 0.01 if rand < 0.5 # sometimes it takes time
        yield nil, OpenStruct.new(name: "Jo") if block_given?
    end
    end

References:

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_

