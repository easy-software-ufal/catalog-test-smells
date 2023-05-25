Hidden Test Call
^^^^^
**Definition:**

* Tests calling other tests


**Code Example:**

.. code-block:: csharp

  [TestFixture] 
  public class HiddenTestCall { 
    private LogAnalyzer logan; 

    [Test]
    public void CreateAnalyzer_GoodNameAndBadNameUsage() { 
      logan.new LogAnalyzer();
      logan.Initialize(); 
      bool valid = logan.IsValid("abc");
      Assert.That(valid, Is.False);
      CreateAnalyzer_GoodFileName_ReturnsTrue(); 
    } 
    
    [Test]
    public void CreateAnalyzer_GoodFileName_ReturnsTrue() { 
      bool valid = logan.IsValid("abcdefg"); 
      Assert.That(valid. Is.True);
    }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Chapter 8. The pillars of good unit tests <https://apprize.best/c/unit/8.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
