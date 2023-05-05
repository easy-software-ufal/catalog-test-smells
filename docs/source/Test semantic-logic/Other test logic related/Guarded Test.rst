Guarded Test
^^^^^
Definition:

* Guarded Tests include boolean branching logics like ifTrue: or ifFalse:
* Conditional test including branches like ifTrue:aBlock or ifFalse:aBlock


Code Example:

.. code-block::

  testRendering
    self shouldRun ifFalse: [ ^ true ].
    self assert: ...
    ...

References:

 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_
 * `Rule-based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_

