Fully Rotten Green Test
^^^^^
**Definition:**

* Contains an assertion which was forced to fail.


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

* `RTj: a Java framework for detecting and refactoring rotten green test cases <https://dl.acm.org/doi/10.1145/3377812.3382151>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`

