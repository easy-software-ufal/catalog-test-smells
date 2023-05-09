Duplicate Component Definition
^^^^^
**Definition:**

* Two or more components declare identical variables, constants, timers or ports.


**Code Example:**

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


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
* `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

