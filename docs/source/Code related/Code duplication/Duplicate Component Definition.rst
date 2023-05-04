Duplicate Component Definition
^^^^^
Definitions:

* Two or more components declare identical variables, constants, timers or ports.


Code Example:

.. code-block::

    type component c1 { 
        var integer i ; 
        const integer id := 1; 
        timer t; 
        port ExamplePort p1; 
    } 

    type component c2 { 
        const integer id := 2; 
        timer t; 
        port ExamplePort p2; 
    } 


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

