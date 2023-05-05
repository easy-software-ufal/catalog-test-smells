Duplicate Alt Branches
^^^^^
Definition:

* Different alt constructs contain duplicate branches


Code Example:

.. code-block:: java

    testcase tc_example_TestCase1() runs on ExampleComponent {
        timer t_guard ;
        // . . .
        t_guard.start(10.0) ;
        alt{
            [] pt.receive(a_MessageOne){
            pt.send(a_MessageTwo);
            }
            [] any port.receive {
            set.verdict(fail);
            stop;
            }
            [] t_guard.timeout{
            set.verdict(fail);
            stop;
        }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

