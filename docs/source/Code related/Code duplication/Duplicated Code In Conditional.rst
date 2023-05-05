Duplicated Code In Conditional
^^^^^
Definitions:

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

