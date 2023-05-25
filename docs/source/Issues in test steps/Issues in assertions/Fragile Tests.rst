Fragile Test
^^^^^
**Definition:**

* Tests which seem to break when they shouldn't


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

* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_ :octicon:`graph;1em`
* `Rails Testing Antipatterns <https://thoughtbot.com/upcase/videos/testing-antipatterns>`_ :octicon:`file-code;1em` :octicon:`sync;1em`
* `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_
* `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
