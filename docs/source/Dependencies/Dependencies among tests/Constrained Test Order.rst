Constrained Test Order
^^^^^
Definition:

* Tests expecting to be run in a specific order or expecting information from other test results


Code Example:

.. code-block:: csharp

  [TestFixture]
  public class IsolationsAntiPatterns
  {
    private LogAnalyzer logan;

    [Test]
    public void CreateAnalyzer_BadFileName_ReturnsFalse()
    {
      logan = new LogAnalyzer();

      logan.Initialize();

      bool valid = logan.IsValid("abc");

      Assert.That(valid, Is.False);
    }

    [Test]
    public void CreateAnalyzer_GoodFileName_ReturnsTrue()
    {
      bool valid = logan.IsValid("abcdefg");

      Assert.That(valid, Is.True);
    }

  }

References:

 * `Chapter 8. The pillars of good unit tests <https://apprize.best/c/unit/8.html>`_

