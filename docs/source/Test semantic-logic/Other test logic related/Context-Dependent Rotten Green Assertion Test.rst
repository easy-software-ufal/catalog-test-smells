Context-Dependent Rotten Green Assertion Test
^^^^^
**Definition:**

* Tests contain multiple conditional branches with different assertions in each branch


**Code Example:**

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

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Rotten green tests in Java, Pharo and Python <https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/article/10.1007/s10664-021-10016-2&casa_token=8C-rVSu9l74AAAAA:2s5rmzBFiH74xHZlTdpZsQCxwqL4cYIbWRH6Bdq1ehTjnxcpOwi8PPkhDrhKpHqjdrQf1_ZXaVRy5BysSQ>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `RTj: a Java framework for detecting and refactoring rotten green test cases <https://dl.acm.org/doi/10.1145/3377812.3382151>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
