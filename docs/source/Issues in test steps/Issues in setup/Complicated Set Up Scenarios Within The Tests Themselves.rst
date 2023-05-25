Complicated Set Up Scenarios Within The Tests Themselves
^^^^^
**Definition:**

* Whilst there’s a place for automated end-to-end scenarios (I call these user journies), I prefer most acceptance tests to jump straight to the point.


**Code Example:**

.. code-block:: text

    Scenario: Accept Visa and Mastercard for Australia
    Given I am on the home page for Australia
    And I choose the tea menu
    And I select some 'green tea'
    And I add the tea to my basket
    And I choose to checkout
    Then I should see 'visa' is accepted
    And I should see 'mastercard' is accepted


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Five automated acceptance test anti-patterns <https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_ :octicon:`file-code;1em`
