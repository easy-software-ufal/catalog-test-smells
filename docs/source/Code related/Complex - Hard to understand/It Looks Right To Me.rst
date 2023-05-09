It Looks Right To Me
^^^^^
Definition:

* Where the test data for negative cases makes the test hard to understand


Code Example:

.. code-block:: java

    expect(getFieldCaseInsensitive(obj, 'username'))
    .toEqual('Mr User');
    
    expect(getFieldCaseInsensitive(obj, 'Username'))
    .toEqual('Mr User');
    
    expect(getFieldCaseInsensitive(obj, 'UserNaME'))
    .toEqual('Mr User');



References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

