Context-Dependent Rotten Green Assertion Test
^^^^^
Definition:

* Tests contain multiple conditional branches with different assertions in each branch


Code Example:

.. code-block:: java

  @Test public void testCoGroupLambda(){
    CoGroupFunction<Tuple2<...>> f = (i1,i2,o) -> { } ;
    TypeInformation<?> ti = TypeExtractor.getCoGroupReturnTypes(f, . . . ) ;

    if (!(ti instanceof MissingTypeInfo)){
      assertTrue(ti.isTupleType());
      assertEquals(2, ti.getArity());
      . . .
    }

  }

References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `RTj: a Java framework for detecting and refactoring rotten green test cases <https://dl.acm.org/doi/10.1145/3377812.3382151>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`

