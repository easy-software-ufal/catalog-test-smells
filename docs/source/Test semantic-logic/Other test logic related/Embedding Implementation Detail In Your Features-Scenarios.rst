Embedding Implementation Detail In Your Features/Scenarios
^^^^^
Definition:

* Acceptance test scenarios are meant to convey intention over implementation. If you start seeing things like URLs in your test scenarios you’re focusing on implementation.


Code Example:

    Scenario: Social media links displayed on checkout page
    Given I am the checkout page for Australia
    Then I should see a link to 'http://twitter.com/beautifultea'
    And I should see a link to 'https://facebook.com/beautifultea'
 
References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Five automated acceptance test anti-patterns <https://web.archive.org/web/20211113081220/https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_ :octicon:`file-code;1em`

