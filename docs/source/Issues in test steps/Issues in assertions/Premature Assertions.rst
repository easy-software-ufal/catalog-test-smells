Premature Assertions
^^^^^
Definition:

* Intermingled with a test's set-up of the data and objects it depends on are assertions which attempt to ensure that set-up was successful. The net effect of this often resembles a "Arrange-Assert-Act-Assert" pattern.


Code Example:

.. code-block:: ruby

  # Subject under test
  class Plane
    def initialize(air_traffic_control)
      @air_traffic_control = air_traffic_control
    end

    def take_off
      if started? &&
          on_airstrip? &&
          @air_traffic_control.ready_for_takeoff?(self)
        (rand * 1000).round
      else
        0
      end
    end
  end


  # Test
  class PrematureAssertions < SmellTest
    def setup
      @air_traffic_control = AirTrafficControl.new
      @plane = Plane.new(@air_traffic_control)
      super
    end

    def test_take_off_when_ready
      @plane.start
      assert_equal true, @plane.started?
      @plane.taxi
      assert_equal true, @plane.on_airstrip?
      @air_traffic_control.approve(@plane)
      assert_equal true, @air_traffic_control.ready_for_takeoff?(@plane)

      altitude = @plane.take_off

      assert altitude > 0, "altitude should be greater than 0"
    end

    def test_does_not_take_off_when_not_ready
      altitude = @plane.take_off

      assert_equal 0, altitude
    end
  end

  # Fake production implementations to simplify example test of subject
  class Plane
    def start
      @started = true
    end

    def started?
      @started if defined?(@started)
    end

    def taxi
      @taxied = true
    end

    def taxied?
      @taxied
    end

    def on_airstrip?
      taxied?
    end
  end

  class AirTrafficControl
    def approve(plane)
      @approved = true
    end

    def ready_for_takeoff?(plane)
      @approved
    end
  end

References:

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

