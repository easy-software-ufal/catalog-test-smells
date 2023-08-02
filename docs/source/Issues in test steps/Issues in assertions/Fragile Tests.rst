Fragile Test
^^^^^
**Definition:**

* Tests which seem to break when they shouldn't


**Also Known As:**

* Brittle Test


**Code Example:**

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

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_ :octicon:`graph;1em`
