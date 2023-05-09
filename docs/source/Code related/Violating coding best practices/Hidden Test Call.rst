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

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Chapter 8. The pillars of good unit tests <https://apprize.best/c/unit/8.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

