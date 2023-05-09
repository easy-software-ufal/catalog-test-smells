Chatty Logging
^^^^^
Definition:

* Often a substitute for self-explanatory assertions or well defined test names, the test writes lots of data to the console or logs in order to explain test failures outside of the assertions


Code Example:

.. code-block:: java

    public class LoginTest {
        private WebDriver driver;
        
        @Before
        public void setUp() {
            driver = new ChromeDriver();
            driver.manage().window().maximize();
        }
        
        @After
        public void tearDown() {
            driver.quit();
        }

        @Test
        public void testValidLogin() {
            LoginPage loginPage = new LoginPage(driver);
            loginPage.enterUsername("testuser");
            loginPage.enterPassword("password");
            loginPage.clickLoginButton();
            
            String expectedUrl = "https://example.com/dashboard";
            String actualUrl = driver.getCurrentUrl();
            
            if (actualUrl.equals(expectedUrl)) {
                System.out.println("Login test passed.");
            } else {
                System.out.println("Login test failed. Expected URL: " + expectedUrl + ", Actual URL: " + actualUrl);
            }
            
            assertTrue(actualUrl.equals(expectedUrl));
        }
    }


References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

