Invasion Of Privacy
^^^^^
**Definition:**

* A test is written directly against a method that's intended to be a private implementation detail of the subject.


**Code Example:**

.. code-block:: ruby

  # Subject under test
  class SeatMap
    def initialize(ticket, original_seat)
      @fare_class = ticket.fare_class
      @current_seat = original_seat
    end

    def moveTo(new_seat)
      raise "No seat selected" unless new_seat
      raise "Invalid seat selected" unless /^\d\d?[A-J]$/.test(new_seat)

      if qualify_fare_class_for_seat(new_seat)
        @current_seat = new_seat
      else
        raise Error "Seat not available for ticket's fare class"
      end
    end

    private

    # Private API! Don't call this!
    def qualify_fare_class_for_seat(seat)
      return unless seat

      if row_match = seat.match(/^(\d+)/)
        row = row_match[0].to_i
        row > 10
      end
    end
  end

  # Test
  class InvasionOfPrivacy < SmellTest
    def setup
      @ticket = OpenStruct.new(fare_class: "M")
      @subject = SeatMap.new(@ticket, "18D")
      super
    end

    def test_ensure_seat_not_null
      result = @subject.send(:qualify_fare_class_for_seat, nil)

      refute result
    end

    def test_do_not_break_if_seat_lacks_a_row_number
      result = @subject.send(:qualify_fare_class_for_seat, "A")

      refute result
    end

    def test_approve_if_behind_row_ten
      result = @subject.send(:qualify_fare_class_for_seat, "11B")

      assert_equal true, result
    end

    def test_deny_if_ahead_of_row_ten
      result = @subject.send(:qualify_fare_class_for_seat, "9J")

      refute result
    end
  end

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Smells in Software Test Code: A Survey of Knowledge in Industry and Academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_

