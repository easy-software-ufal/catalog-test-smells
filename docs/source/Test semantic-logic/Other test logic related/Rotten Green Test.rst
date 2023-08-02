Rotten Green Test
^^^^^
**Definition:**

* A test that passes (is green) but contains assertions that are never executed


**Code Example:**

.. code-block:: java

  @Test
  public void testListWindowsNewBucket() throws Exception {
    . . .
    BucketLeapArray leapArray = new BucketLeapArray(sampleCount,
            intervalInMs);
    . . . .
    List<WindowWrap<MetricBucket>> list = leapArray.list();
    for (WindowWrap<MetricBucket> wrap : list) {
      assertTrue(windowWraps.contains(wrap));
    }
    . . . .
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Detection of test smells with basic language analysis methods and its evaluation <https://ieeexplore.ieee.org/document/10123551/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `JTDog: a Gradle Plugin for Dynamic Test Smell Detection <https://ieeexplore.ieee.org/document/9678529/>`_ :octicon:`comment-discussion;1em`
* `RTj: a Java framework for detecting and refactoring rotten green test cases <https://dl.acm.org/doi/10.1145/3377812.3382151>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
