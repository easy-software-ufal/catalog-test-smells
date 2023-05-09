Ground Zero
^^^^^
Definition:

* Where the lack of testing with 0 is the source of a lot of bugs.


Code Example:

.. code-block:: javascript
  
  // ensuring that there’s a value for and then testing that it’s off screen
  // but if element.top is equals to 0, results goes wrong
  if (element.top && (element.top < viewport.top)) {
   hidePane();
  }

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

