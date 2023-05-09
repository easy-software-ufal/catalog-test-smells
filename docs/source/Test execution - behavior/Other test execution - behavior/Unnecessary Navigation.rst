Unnecessary Navigation
^^^^^
Definition:

* When the test has actions, taken for granted, not related to the things we want to check


Code Example:

.. code-block:: csharp

  public void CheckBookTitleDescriptionAndPrice_Version1()
  {
      foreach (Book currentBook in testFile)
      {
          // Open the homepage
          selenium.Open("/HomePage.html");
          selenium.WaitForPageToLoad("30000");
  
          // Login
          selenium.Click("link=Login");
          selenium.WaitForPageToLoad("30000");
          selenium.Type("TxtUserName", "TestAccount1");
          selenium.Type("TxtPassword", "TestPassword1");
          selenium.Click("Submit");
          selenium.WaitForPageToLoad("30000");
  
          // Search for the book we want to check
          selenium.Click("link=Search");
          selenium.WaitForPageToLoad("30000");
          selenium.Type("TxtSearchTerm", currentBook.Title);
          selenium.Click("Submit");
          selenium.WaitForPageToLoad("30000");
  
        // Open the Detailed Information page for the book we want to check<br />
          selenium.Click(currentBook.ID);
          selenium.WaitForPageToLoad("30000");
  
          // Check that the Detailed Information page has loaded
          Assert.AreEqual("Detailed Information page", selenium.GetTitle());
          
          // Compare the information on the Detailed Information page to our expected results
          string actualBookTitle = selenium.GetText("BookTitle" + currentItem.ID);
          Assert.AreEqual(actualBookTitle, currentBook.Title);
          
          string actualBookDescription = selenium.GetText("BookDescription" + currentItem.ID);
          Assert.AreEqual(actualBookDescription, currentBook.Description);
          
          string actualBookPrice = selenium.GetText("BookPrice" + currentItem.ID);
          Assert.AreEqual(actualBookPrice, currentBook.Price);
      }
  }

References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `How test automation with selenium can fail <https://mattarcherblog.wordpress.com/2010/11/29/how-test-automation-with-selenium-or-watir-can-fail/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

