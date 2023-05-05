Duplicated Code In Conditional
^^^^^
Definition:

* The duplicated code can appear in a series of conditionals (with different conditions and the same action in each check) or in all legs of a conditional


Code Example:

.. code-block:: java

    function checkSomething(in float p1, in float p2) return boolean {
        if (p1 < 0.0) {
            return false;
        }
        if (p2 >= 7.0) {
            return false;
        }
        if (p2 < p1) {
            return false;
        }
        return true;
    }

    function checkSomethingElse(in float p1) runs on ExampleComponent {
        var charstring result;
        if (p1 > 0) {
            result := "foo";
            pt.send(result);
        } else {
            result := "bar";
            pt.send(result);
        }
    }



References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

