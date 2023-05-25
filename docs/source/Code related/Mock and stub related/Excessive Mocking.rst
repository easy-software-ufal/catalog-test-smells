Excessive Mocking
^^^^^
**Definition:**

* Refers to a test case which requires many mocks to run [35, 45]. The system under test may need a complex environment, specific resources, or depend on 3rd party systems which cannot be provided during test execution. Running tests against a database is a canonical example. If the database isn’t available, all tests will fail even though the system under test might be completely bug-free. A common solution is to mock those potential failures by mimicking the behavior of real objects. Developers also use mocks when testing authentication, but sometimes struggle with strategy.


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_ :octicon:`comment-discussion;1em`
* `Unit Testing Smells: What Are Your Tests Telling You? <https://dzone.com/articles/unit-testing-smells-what-are-your-tests-telling-yo>`_ :octicon:`comment-discussion;1em`
