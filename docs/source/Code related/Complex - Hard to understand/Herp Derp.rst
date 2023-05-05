Herp Derp
^^^^^
Definitions:

* Words and comments in test code or names that add nothing, like simple or test or //given


Code Example:

.. code-block:: text

    #. Calling the test method test in any way – we know it’s a test, get on with it
    #. Weak adjective expressions like simple – what makes it simple?
    #. Commenting a line of code with a description of what that line’s implementation is doing – e.g. // assert that it's true – we can see what it’s doing… WHY is it doing it?
    #. Pasting in the same comments from other tests whether or not they’re relevant – this is probably a case for reducing boilerplate so you don’t need as much paste, or as much comment
    #. Naming test inputs and outputs after their type, rather than their purpose in the test – e.g. String string1 = code.getUserName()

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

