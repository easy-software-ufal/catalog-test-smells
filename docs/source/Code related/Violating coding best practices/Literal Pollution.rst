Literal Pollution
^^^^^
Definition:

* When writing tests for the application code it is mostly required also to provide some data to be able to test the functionality. This is mostly done by defining literals in the test code. However an excessive use of literals can cause severe problems:
  * Too many literals are distracting and obfuscate the functionality and purpose of a test. This makes a test hard to read and understand. 
  * The same or similar test data is often repeated within a test or testsuite. This is often a consequence of simply extending or adding tests without actually designing them. The result is a test-suite that is extremely hard to maintain and refactor. We detected such Duplication in harvesting our case study.


Code Example:

.. code-block::

  UrlTest >> #testUsernamePasswordPrinting
    #(’http://user:pword@someserver.blah:8000/root/index.html’
    ’http://user@someserver.blah:8000/root/index.html’
    ’http://user:pword@someserver.blah/root/index.html’
    ) do: [ :urlText | self should: [ urlText = urlText asUrl asString ] ].


References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

