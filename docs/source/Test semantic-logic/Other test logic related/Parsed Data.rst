Parsed Data
^^^^^
Definition:

* A test creates structured data by parsing unstructured input and only uses the structured data during the test.


Code Example:

.. code-block:: java

  void ParseAndTest(string xml) {
    // parse
    Employee e = Employee.Deserialize(xml);
    // test logic
    EmployeeCollection c = new EmployeeCollection();
    c.Add(e);
    Assert.IsTrue(c.Contains(e));
  }

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Parameterized Test Patterns For Effective Testing with Pex <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.159.6145&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

