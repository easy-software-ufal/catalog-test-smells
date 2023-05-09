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

 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Rule-Based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_

