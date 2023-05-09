Skip Rotten Green Test
^^^^^
Definition:

* Contains guards to stop their execution early under certain conditions.


Code Example:

.. code-block:: java

  @Test public void testNormalizedKeyReadWriter(){
     . . .
     TypeComparator <T> comp1 = getComparator(true);

     if(!comp1.supportsSerializationWithKeyNormalization()){
      return ;
     }
     . . .
     assertTrue(comp1.compareToReference(comp2) == 0);
     . . .
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `RTj: a Java framework for detecting and refactoring rotten green test cases <https://dl.acm.org/doi/10.1145/3377812.3382151>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`

