Exception Handling
^^^^^
Definition:

* This smell occurs when a test method explicitly a passing or failing of a test method is dependent on the production method throwing an exception. Developers should utilize JUnit's exception handling to automatically pass/fail the test instead of writing custom exception handling code or throwing an exception.


Code Example:

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
    

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_ :octicon:`file-code;1em`
 * `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
 * `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
 * `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
 * `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
 * `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
 * `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_

