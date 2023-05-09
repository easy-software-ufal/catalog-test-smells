Fragile Tests
^^^^^
Definition:

* Tests which seem to break when they shouldn't


Code Example:

.. code-block:: ruby

  describe Post do
    let(:user) { build_stubbed(:user) }
    let(:title) { "Example Post" }
    subject(:post) { build_stubbed(:post, user: user, title: title) }

    # ...

    context "with an author" do
      let(:user) { build_stubbed(:user, name: "Willy") }

      it "returns the author's name" do
        expect(post.author_name).to eq("Willy")
      end
    end
  end

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Rails Testing Antipatterns <https://thoughtbot.com/upcase/videos/testing-antipatterns>`_ :octicon:`file-code;1em`

