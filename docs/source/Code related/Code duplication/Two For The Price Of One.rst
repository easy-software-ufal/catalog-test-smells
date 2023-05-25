Two For The Price Of One
^^^^^
**Definition:**

* Sometimes a sign of missing parameterised tests – where a single test case is testing two use cases with the same set up


**Code Example:**

.. code-block:: java

    private LocalDateTime now = LocalDateTime.now();
    private LocalDateTime tomorrow = LocalDateTime.plus(1, DAYS);
    private LocalDateTime yesterday = LocalDateTime.minus(1, DAYS);
    
    @Test
    public void dateComparisonWorksForPastAndFuture() {
        assertDateComparison(now, tomorrow, "is in the future");
        assertDateComparison(now, yesterday, "is in the past");
    }
    
    private void assertDateComparison(LocalDateTime baseline,
                                    LocalDateTime compare,
                                    String expected) {
        assertEquals(expected, MyDates.describe(baseline, compare);
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`
