Transcripting Test
^^^^^
**Definition:**

* A Transcripting Test is writing information to the console or a global stream, for example the Transcript in Smalltalk, while it is running.


**Code Example:**

.. code-block:: smalltalk

  HeapTest >> #testExamples
    self shouldnt: [ self heapExample ] raise: Error.
    self shouldnt: [ self heapSortExample ] raise: Error.

  HeapTest >> #heapSortExample
    "HeapTest new heapSortExample"
    "Sort a random collection of Floats and compare the results with ... ''
    | n rnd array time sorted |
    n := 10000. "# of elements to sort"
    rnd := Random new.
    
    Transcript cr; show:'Time for heap-sort: ', time printString,' msecs'.
    "The quicksort version"
    
    Transcript cr; show:'Time for quick-sort: ', time printString,' msecs'.
    "The merge-sort version"

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Rule-based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
