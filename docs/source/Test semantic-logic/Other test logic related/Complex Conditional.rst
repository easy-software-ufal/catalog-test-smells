Complex Conditional
^^^^^
Definitions:

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

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

