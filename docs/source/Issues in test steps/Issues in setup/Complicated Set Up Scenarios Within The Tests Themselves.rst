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

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Five automated acceptance test anti-patterns <https://web.archive.org/web/20211113081220/https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_ :octicon:`file-code;1em`

