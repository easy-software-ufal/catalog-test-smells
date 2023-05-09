Test By Number
^^^^^
Definition:

* Production code is tested consistently by rote, inadvertently suppressing creativity in the design of both the tests and their subjects.


Code Example:

.. code-block:: ruby
    
  # Test
  class TestByNumber < SmellTest
    def setup
      @repo = Repo.new
      @subject = AddressController.new(@repo)
      super
    end

    def test_create
      user = @repo.save(OpenStruct.new(name: 'Jane', addresses: []))
      address_params = OpenStruct.new(street: 'some street')

      @subject.create(user, address_params)

      address = @repo.find(address_params.id)
      assert_equal "some street", address.street
      assert_equal address, user.addresses[0]
    end

    def test_read
      address = @repo.save(OpenStruct.new(street: 'a street'))
      user = @repo.save(OpenStruct.new(name: 'Joe', addresses: [address]))

      result = @subject.read(user, address.id)

      assert_equal address, result
    end

    def test_update
      address = @repo.save(OpenStruct.new(street: 'no street', zip: '12345'))
      user = @repo.save(OpenStruct.new(name: 'Jill', addresses: [address]))

      @subject.update(user, {
        id: address.id,
        street: 'the street'
      })

      address = @repo.find(address.id)
      assert_equal "the street", address.street
      assert_equal "12345", address.zip
    end

    def test_destroy
      address = @repo.save(OpenStruct.new(street: 'foo street'))
      user = @repo.save(OpenStruct.new(name: 'Gene', addresses: [address]))

      @subject.destroy(user, address.id)

      assert_equal nil, @repo.find(address.id)
      assert_equal 0, user.addresses.length
    end

    # Fake production implementations to simplify example test of subject
    class Repo
      def initialize
        @items = {}
        @next_id = 1
      end

      def save(item)
        item.id = item.id || @next_id += 1
        @items[item.id] = item
        return item
      end

      def find(item_id)
        @items[item_id]
      end

      def destroy(item_id)
        @items.delete(item_id)
      end
    end
  end


References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

