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

 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_
 * `Rule-based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_

