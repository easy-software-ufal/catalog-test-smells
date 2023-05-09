Complex Conditional
^^^^^
Definition:

* A conditional expression is composed of many boolean conjunctions.


Code Example:

.. code-block:: pseudo

  function calculateAmount(integer year) return float {
    var float amount;
    if (( (year mod 4) == 0 and not (year mod 100) == 0 ) or (year mod 400) == 0 ) {
      amount := BASE AMOUNT ∗ 366;
    } else {
      amount := BASE AMOUNT ∗ 365;
    }
    return amount;
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

