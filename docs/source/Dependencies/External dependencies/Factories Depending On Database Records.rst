Factories Depending On Database Records
^^^^^
Definition:

* Adding a hard dependency on specific database records in factory definitions leads to build failures in CI environment.


Code Example:

.. code-block:: ruby

  factory :active_schedule do
    start_date Date.current - 1.month
    end_date 1.month.since(Date.current)
    processing_status "processed"
    schedule_duration ScheduleDuration.find_by_name("Custom")
  end

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Rails Testing Antipatterns: Fixtures and Factories <https://semaphoreci.com/blog/2014/01/14/rails-testing-antipatterns-fixtures-and-factories.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

