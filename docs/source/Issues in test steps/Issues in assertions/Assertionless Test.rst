Assertionless Test
^^^^^
Definition:

* A test that does not contain at least one valid assertion is not a real test as it does only execute plain source-code, but never assert any data, state or functionality.
* Pretending to assert data and functionality, but does not


Code Example:

.. code-block:: Smalltalk

  // Smalltalk
  ICCreateCalendar>>TesttestCreatingSeveralCalendars
    self addCalendarWithName: ’new Calendar 1’.
    self addCalendarWithName: ’new Calendar 2’.
    self addCalendarWithName: ’new Calendar 3’.
    self addCalendarWithName: ’new Calendar 1’.
    self addCalendarWithName: ’new Calendar 2’.
    self addCalendarWithName: ’new Calendar 3’.


References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Rule-Based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
 * `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_

