Coupling Between Test Methods
^^^^^
**Definition:**

* Test methods (and all tests in general) must be perfectly isolated from each other. This means that changing one test must not affect any others.


**Code Example:**

.. code-block:: java

  public final class MetricsTest {
    private File temp;
    private Folder folder;
    @Before
    public void prepare() {
      this.temp = Files.createTempDirectory("test");
      this.folder = new DiscFolder(this.temp);
      this.folder.save("first.txt", "Hello, world!");
      this.folder.save("second.txt", "Goodbye!");
    }
    @After
    public void clean() {
      FileUtils.deleteDirectory(this.temp);
    }
    @Test
    public void calculatesTotalSize() {
      assertEquals(22, new Metrics(this.folder).size());
    }
    @Test
    public void countsWordsInFiles() {
      assertEquals(4, new Metrics(this.folder).wc());
    }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `A few thoughts on unit test scaffolding <https://www.yegor256.com/2015/05/25/unit-test-scaffolding.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

