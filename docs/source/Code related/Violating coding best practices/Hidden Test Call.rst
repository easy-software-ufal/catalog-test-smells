Hidden Test Call 
^^^^^
Definition:

* Tests calling other tests


Code Example:

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

References:

 * `Chapter 8. The pillars of good unit tests <https://apprize.best/c/unit/8.html>`_

