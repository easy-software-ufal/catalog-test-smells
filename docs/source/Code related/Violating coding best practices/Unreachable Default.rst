Unreachable Default
^^^^^
Definitions:

* An alt statement contains an else branch while a default is active. The else branch of an alt statement is taken if no other branch is applicable. If a default is active at the same time, its branches come after all branches of the alt statement. Hence the default altstep can never be executed if an else branch is present.


Code Example::

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

