Overreferencing
^^^^^
Definition:

* It is about test-methods referencing many times classes from the application code. The main problem with an Overreferencing Test is that it causes a lot of unnecessary dependencies towards the model code. That distracts from the goal of the test.
* Test creating unnecessary dependencies and causing duplication


Code Example:

.. code-block:: pseudo

  BooleanTypesTest >> #testTrueFalseSubtype
    | system boolType boolMetaType |
    system := TPStructuralTypeSystem new.

    boolType := TPClassType on: Boolean.
    
    self assert: (system is: (TPClassType on: True) subtypeOf: boolType).

    self assert: (system is: (TPClassType on: False) subtypeOf: boolType).

    self assert: (system is: (TPClassType on: False) subtypeOf: (TPClassType on: True)).

    self assert: (system is: (TPClassType on: True) subtypeOf: (TPClassType on: False)).

    boolMetaType := TPClassType on: Boolean class.

    self assert: (system is: (TPClassType on: True class) subtypeOf: boolMetaType).

    self assert: (system is: (TPClassType on: False class) subtypeOf: boolMetaType).

    self assert: (system is: (TPClassType on: False class) subtypeOf: (TPClassType on: True class)).

    self assert: (system is: (TPClassType on: True class) subtypeOf: (TPClassType on: False class)).

References:

 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_
 * `Rule-Based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_

