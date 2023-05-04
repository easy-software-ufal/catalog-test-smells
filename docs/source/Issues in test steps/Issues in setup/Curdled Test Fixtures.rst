Curdled Test Fixtures 
^^^^^
Definitions:

* Where there’s an inappropriate union of tests in the same fixture, or splitting into multiple fixtures where one would be better


Code Example:

..code-block:: java

    class MyTest {
    // some test input or expected output
    private static final SomeObject COMPLEX_DATA = new ...;
    
    private Thing whatWeAreTesting = new ...;
    
    // ... other resources
    
    @BeforeEach
    void beforeEach() {
        // some additional setup
    }
    
    @AfterEach
    void afterEach() {
        // some tidy up
    }
    
    @Test
    void testOne() { ... }
    }

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

