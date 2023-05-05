Half A Helper Method 
^^^^^
Definitions:

* Where there’s a utility method to help a test do its job, yet all calls to it are immediately followed by the exact same code. This is because the method is only doing half the job it should, so your test has more boilerplate in it.


Code Example:

.. code-block :: javascript

    function readFile(filename) {
    // open file and return its string
    }
    
    function substituteId(file, id) {
    const placeholder = 'REPLACE-ME';
    
    // do global replace of the placeholder with id
    // return that
    }
    
    // call site
    const file = readFile('foo.txt');
    const substituted = substituteId(file, currentId);

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

