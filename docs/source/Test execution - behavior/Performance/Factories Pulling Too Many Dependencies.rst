Factories Pulling Too Many Dependencies
^^^^^
Definition:

* Calling one factory may silently create many associated records, which accumulates to make the whole test suite slow (more on that later)


Code Example:

.. code-block:: ruby

  FactoryBot.define do
    factory :comment do
      post
      body "groundbreaking insight"
    end
  end

References

.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Rails Testing Antipatterns: Fixtures and Factories <https://semaphoreci.com/blog/2014/01/14/rails-testing-antipatterns-fixtures-and-factories.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

