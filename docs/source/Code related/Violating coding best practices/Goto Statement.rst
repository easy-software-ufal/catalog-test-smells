Goto Statement
^^^^^
Definition:

* A goto statement is used. The use of goto statements is inadvisable and should be avoided.


Code Example:

.. code-block::

  function f ( integer i ) runs on ExampleComponent {
    var integer MyVar := i ;
    label L1 ;
    MyVar := 2 ∗ MyVar ;
    if (MyVar < 2000) {
      goto L1 ;
    }
    MyVar2 := f2(MyVar);
    if (MyVar2 > MyVar) {
      goto L2 ;
    }
    p.send(MyVar);
    p.receive -> value MyVar2;
    label L2 ;
  }


References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

