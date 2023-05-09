Missed Skip Rotten Green Test
^^^^^
Definition:

* Test methods contain guards to stop their execution early under certain conditions.


Code Example:

.. code-block:: java

    @Test
        public void testNormalizedKeysGreatSmallAscDescHalfLenght(){
        TypeComparator<T> comparator = getComparator(true);
        if (not(comparator.supportsNormalizedKey())){
            return;
        }
        testNormalizedKeysGreatSmall(true, comparator,true);
        testNormalizedKeysGreatSmall(false, comparator,true);
        }
References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Rotten green tests in Java, Pharo and Python <https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/article/10.1007/s10664-021-10016-2&casa_token=8C-rVSu9l74AAAAA:2s5rmzBFiH74xHZlTdpZsQCxwqL4cYIbWRH6Bdq1ehTjnxcpOwi8PPkhDrhKpHqjdrQf1_ZXaVRy5BysSQ>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

