Missed Fail Rotten Green Test
^^^^^
Definition:

* Tests where the test engineer passes to an assertion primitive to force the test to fail. Such assertion calls are intended to be executed only if something goes wrong, and not if the test passes.


Code Example:

.. code-block:: java

    @Test
    public void testMethod() {
        MyClass obj = new MyClass();
        int expected = 5;
        int actual = obj.doSomething();
        assertTrue(actual > 0);
        assertFalse(actual > 10);
        fail("Something went wrong");
    }

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Rotten green tests in Java, Pharo and Python <https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/article/10.1007/s10664-021-10016-2&casa_token=8C-rVSu9l74AAAAA:2s5rmzBFiH74xHZlTdpZsQCxwqL4cYIbWRH6Bdq1ehTjnxcpOwi8PPkhDrhKpHqjdrQf1_ZXaVRy5BysSQ>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `RTj: a Java framework for detecting and refactoring rotten green test cases <https://dl.acm.org/doi/10.1145/3377812.3382151>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`

