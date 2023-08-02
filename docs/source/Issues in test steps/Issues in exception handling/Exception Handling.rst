Exception Handling
^^^^^
**Definition:**

* This smell occurs when a test method explicitly a passing or failing of a test method is dependent on the production method throwing an exception. Developers should utilize JUnit's exception handling to automatically pass/fail the test instead of writing custom exception handling code or throwing an exception.


**Code Example:**

.. code-block:: java

  @Test
  public void realCase() {
      Point p34 = new Point("34", 556506.667, 172513.91, 620.34, true);
      Point p45 = new Point("45", 556495.16, 172493.912, 623.37, true);
      Point p47 = new Point("47", 556612.21, 172489.274, 0.0, true);
      Abriss a = new Abriss(p34, false);
      a.removeDAO(CalculationsDataSource.getInstance());
      a.getMeasures().add(new Measure(p45, 0.0, 91.6892, 23.277, 1.63));
      a.getMeasures().add(new Measure(p47, 281.3521, 100.0471, 108.384, 1.63));

      try {
          a.compute();
      } catch (CalculationException e) {
          Assert.fail(e.getMessage());
      }

      // test intermediate values with point 45
      Assert.assertEquals("233.2405",
          this.df4.format(a.getResults().get(0).getUnknownOrientation()));
      Assert.assertEquals("233.2435",
          this.df4.format(a.getResults().get(0).getOrientedDirection()));
      Assert.assertEquals("-0.1", this.df1.format(
          a.getResults().get(0).getErrTrans()));

      // test intermediate values with point 47
      Assert.assertEquals("233.2466",
          this.df4.format(a.getResults().get(1).getUnknownOrientation()));
      Assert.assertEquals("114.5956",
          this.df4.format(a.getResults().get(1).getOrientedDirection()));
      Assert.assertEquals("0.5", this.df1.format(
          a.getResults().get(1).getErrTrans()));

      // test final results
      Assert.assertEquals("233.2435", this.df4.format(a.getMean()));
      Assert.assertEquals("43", this.df0.format(a.getMSE()));
      Assert.assertEquals("30", this.df0.format(a.getMeanErrComp()));
  }
    

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Automatic Identification of High-Impact Bug Report by Product and Test Code Quality <https://huang.zj.cn/pdf/J13.pdf>`_
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`comment-discussion;1em`
* `Characterizing High-Quality Test Methods: A First Empirical Study <https://ieeexplore.ieee.org/document/9796158/>`_ :octicon:`graph;1em`
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the diffusion of test smells and their relationship with test code quality of Java projects <https://onlinelibrary.wiley.com/doi/abs/10.1002/smr.2532>`_ :octicon:`graph;1em`
* `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `On the influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the test smells detection: an empirical study on the jnose test accuracy <https://sol.sbc.org.br/journals/index.php/jserd/article/view/1893>`_ :octicon:`graph;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Pytest-Smell: a smell detection tool for Python unit tests <https://dl.acm.org/doi/10.1145/3533767.3543290>`_ :octicon:`graph;1em`
* `Refactoring Test Smells With JUnit 5: Why Should Developers Keep Up-to-Date? <https://ieeexplore.ieee.org/document/9769994/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_ :octicon:`file-code;1em` :octicon:`sync;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `TEMPY: Test Smell Detector for Python <https://dl.acm.org/doi/10.1145/3555228.3555280>`_ :octicon:`graph;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `TestAXE: Automatically Refactoring Test Smells Using JUnit 5 Features <https://sol.sbc.org.br/index.php/cbsoft_estendido/article/view/22311>`_ :octicon:`graph;1em` :octicon:`sync;1em`
* `The secret life of test smells-an empirical study on test smell evolution and maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `Understanding Testability and Test Smells <https://www.designite-tools.com/blog/understanding-testability-test-smells>`_
* `Understanding practitioners’ strategies to handle test smells: a multi-method study <https://dl.acm.org/doi/10.1145/3474624.3474639>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `tsDetect: an open source test smells detection tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
