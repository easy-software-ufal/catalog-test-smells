Duplicated Code
^^^^^
**Definition:**

* If you have duplicated code in tests, it makes it harder to refactor the implementation code because you have a disproportionate number of tests to update. Tests should help you refactor with confidence, rather than be a large burden that impedes your work on the code being tested.


**Code Example:**

.. code-block:: java

    assertEqual('Joe', person.getFirstName())
    assertEqual('Bloggs', person.getLastName())
    assertEqual(23, person.getAge())

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A Refactoring Tool for TTCN-3 <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.115.3594&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_ :octicon:`graph;1em`
* `Is duplicated code more tolerable in unit tests? <https://stackoverflow.com/questions/129693/is-duplicated-code-more-tolerable-in-unit-tests>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
* `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_
* `Writing good gherkin <https://techbeacon.com/app-dev-testing/7-ways-tidy-your-test-code>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
