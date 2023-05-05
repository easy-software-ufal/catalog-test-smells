Duplicated Code
^^^^^
Definitions:

* If you have duplicated code in tests, it makes it harder to refactor the implementation code because you have a disproportionate number of tests to update. Tests should help you refactor with confidence, rather than be a large burden that impedes your work on the code being tested.


Code Example:

.. code-block::java

    assertEqual('Joe', person.getFirstName())
    assertEqual('Bloggs', person.getLastName())
    assertEqual(23, person.getAge())

References:

 * `Is duplicated code more tolerable in unit tests? <https://stackoverflow.com/questions/129693/is-duplicated-code-more-tolerable-in-unit-tests>`_

