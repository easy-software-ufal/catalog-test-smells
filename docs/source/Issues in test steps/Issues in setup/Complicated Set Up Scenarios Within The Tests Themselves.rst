Complicated Set Up Scenarios Within The Tests Themselves
^^^^^
Definition:

* Whilst there’s a place for automated end-to-end scenarios (I call these user journies), I prefer most acceptance tests to jump straight to the point.


Code Example:

.. code-block:: text

    Scenario: Accept Visa and Mastercard for Australia
    Given I am on the home page for Australia
    And I choose the tea menu
    And I select some 'green tea'
    And I add the tea to my basket
    And I choose to checkout
    Then I should see 'visa' is accepted
    And I should see 'mastercard' is accepted


References:

 * `Five automated acceptance test anti-patterns <https://web.archive.org/web/20211113081220/https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_

nti-patterns//>`_

