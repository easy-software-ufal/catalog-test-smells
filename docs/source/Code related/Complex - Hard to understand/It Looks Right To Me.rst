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



References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

