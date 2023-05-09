Rotten Green Test
^^^^^
Definition:

* A test that passes (is green) but contains assertions that are never executed


Code Example:

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

References:

 * `RTj: a Java framework for detecting and refactoring rotten green test cases <https://dl.acm.org/doi/10.1145/3377812.3382151>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `JTDog: a Gradle Plugin for Dynamic Test Smell Detection <https://ieeexplore.ieee.org/document/9678529/>`_ :octicon:`comment-discussion;1em`
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_

