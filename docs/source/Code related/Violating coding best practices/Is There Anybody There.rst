Is There Anybody There?
^^^^^
Definition:

* Any flickering test that occasionally breaks a build – bad test or bad code?


Code Example:

.. code-block:: java

    @Test
    public void testMethod() {
        int expected = 5;
        int actual = MyUnstableClass.doSomethingWithRandomReturns();
        assertEquals(expected, actual);
    }

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

