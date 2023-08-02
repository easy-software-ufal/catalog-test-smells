Redundant Print
^^^^^
**Definition:**

* Print statements in unit tests are redundant as unit tests are executed as part of an automated. Furthermore, they can consume computing resources or increase execution time if the developer calls an intensive/long-running method from within the print method (i.e., as a parameter).


**Code Example:**

.. code-block:: java

  @Test
  public void testTransform10mNEUAndBack() {
      Leg northEastAndUp10M = new Leg(10, 45, 45);
      Coord3D result = transformer.transform(Coord3D.ORIGIN, northEastAndUp10M);
      System.out.println("result = " + result);
      Leg reverse = new Leg(10, 225, -45);
      result = transformer.transform(result, reverse);
      assertEquals(Coord3D.ORIGIN, result);
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A survey on test practitioners' awareness of test smells <https://arxiv.org/abs/2003.05613>`_
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Automatic Identification of High-Impact Bug Report by Product and Test Code Quality <https://huang.zj.cn/pdf/J13.pdf>`_
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`comment-discussion;1em`
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `How are test smells treated in the wild? A tale of two empirical studies <https://sol.sbc.org.br/journals/index.php/jserd/article/download/1802/1807/7485>`_ :octicon:`graph;1em`
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `On the use of test smells for prediction of flaky tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Pytest-Smell: a smell detection tool for Python unit tests <https://dl.acm.org/doi/10.1145/3533767.3543290>`_ :octicon:`graph;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `TEMPY: Test Smell Detector for Python <https://dl.acm.org/doi/10.1145/3555228.3555280>`_ :octicon:`graph;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `tsDetect: an open source test smells detection tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
