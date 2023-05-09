Litter Bugs
^^^^^
**Definition:**

* Each test has a side effect that persists between test cases, often resulting in tests that depend on one another. This is often called "test pollution"

Also Known As:

* Test Pollution

**Code Example:**

.. code-block:: ruby

  # Subject under test
  $all_time_logins = 0
  class Game
    def self.instance
      @game ||= new
    end

    def initialize
      @players = []
    end

    def add_player(name)
      @players << name
      $all_time_logins += 1
    end

    def player_count
      @players.size
    end
  end

  # Test
  class LitterBugs < SmellTest
    include UnreliableMinitestPlugin

    def setup
      @game = Game.instance
    end

    def test_login_one_player
      @game.add_player("Joe")

      assert_equal 1, @game.player_count
      assert_equal 1, $all_time_logins
    end

    def test_login_two_players
      @game.add_player("Jane")
      @game.add_player("Stef")

      assert_equal 3, @game.player_count
      assert_equal 3, $all_time_logins
    end
  end

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

