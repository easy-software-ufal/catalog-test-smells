Calculating Expected Results On The Fly
^^^^^
**Definition:**

* Any automated test that performs a comparison needs to know the expected results. If you believe that automatically calculating expected results is for you then I would at least consider separating the code that calculates the expected results from the code that performs the actual test.


**Code Example:**

.. code-block:: csharp

  public void CheckWeightCategory_Version1()
  {
      // For each item in the file, check it has been labelled correctly
      foreach (Item currentItem in testFile)
      {
          // Navigate to the item tracking page on the website
          selenium.Open("/ItemTrackingPage.html");
  
        // Get the weight category for the current item
          string acutalWeightCategory = selenium.GetText("weightCategory" + currentItem.ID);
  
          // Calculate the expected result
          string expectedWeightCategory;
  
          // If an item weighs more than 50kg then mark the item as a two-man lift,
          // otherwise mark the item as a one-man lift
          if (currentItem.weight > 50)
          {
              expectedWeightCategory = "two-man lift";
          }
          else
          {
              expectedWeightCategory = "one-man lift";
          }
  
          // Compare actual to expected result
          Assert.AreEqual(acutalWeightCategory, expectedWeightCategory);
      }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `How test automation with selenium can fail <https://mattarcherblog.wordpress.com/2010/11/29/how-test-automation-with-selenium-or-watir-can-fail/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
