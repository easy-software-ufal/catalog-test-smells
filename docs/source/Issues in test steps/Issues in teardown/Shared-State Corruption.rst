Shared-State Corruption
^^^^^
Definition:

* Tests sharing in-memory state without rolling back


Code Example:

.. code-block:: java

  public class SharedStateCorruption
  {
    // shared person state
    Person person = new Person();

    public void CreateAnalyzer_GooFileName_ReturnsTrue()
    {
      // changes shared state
      person.AddNumber("055-4556684(34)");
      string found = person.FindPhoneStartingWith("055");
      Assert.AreEqual("055-4556684(34"), found)
    }

    public void FindPhoneStartingWith_NoNumbers_ReturnNull()
    {
      // reads shared state
      string found = person.FindPhoneStartingWith("0");
      Assert.IsNull(found);
    }
  }

References:

 * `Chapter 8. The pillars of good unit tests <https://apprize.best/c/unit/8.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

