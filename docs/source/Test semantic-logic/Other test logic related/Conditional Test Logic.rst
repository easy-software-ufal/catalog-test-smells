Conditional Test Logic
^^^^^
**Definition:**

* Test methods need to be simple and execute all statements in the production method. Conditions within the test method will alter the behavior of the test and its expected output, and would lead to situations where the test fails to detect defects in the production method since test statements were not executed as a condition was not met. Furthermore, conditional code within a test method negatively impacts the ease of comprehension by developers.


**Also Known As:**

* Indented Test Code

**Code Example:**

.. code-block:: java

  @Test
  public void testSpinner() {
      for (Map.Entry entry : sourcesMap.entrySet()) {

          String id = entry.getKey();
          Object resultObject = resultsMap.get(id);
          if (resultObject instanceof EventsModel) {
              EventsModel result = (EventsModel) resultObject;
              if (result.testSpinner.runTest) {
                  System.out.println("Testing " + id + " (testSpinner)");
                  //System.out.println(result);
                  AnswerObject answer = new AnswerObject(entry.getValue(), "", new CookieManager(), "");
                  EventsScraper scraper = new EventsScraper(RuntimeEnvironment.application, answer);
                  SpinnerAdapter spinnerAdapter = scraper.spinnerAdapter();
                  assertEquals(spinnerAdapter.getCount(), result.testSpinner.data.size());
                  for (int i = 0; i < spinnerAdapter.getCount(); i++) {
                      assertEquals(spinnerAdapter.getItem(i), result.testSpinner.data.get(i));
                  }
              }
          }
      }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A survey on test practitioners' awareness of test smells <https://arxiv.org/abs/2003.05613>`_
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Anti-patterns of automated testing <https://medium.com/swlh/anti-patterns-of-automated-software-testing-b396283a4cb6>`_
* `Automatic Identification of High-Impact Bug Report by Product and Test Code Quality <https://huang.zj.cn/pdf/J13.pdf>`_
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`comment-discussion;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Detection of test smells with basic language analysis methods and its evaluation <https://ieeexplore.ieee.org/document/10123551/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_ :octicon:`comment-discussion;1em`
* `Enhancing developers’ awareness on test suites’ quality with test smell summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `How are test smells treated in the wild? A tale of two empirical studies <https://sol.sbc.org.br/journals/index.php/jserd/article/download/1802/1807/7485>`_ :octicon:`graph;1em`
* `Hunting for smells in natural language tests <https://ieeexplore.ieee.org/abstract/document/6606682>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Improving Student Testing Practices through a Lightweight Checklist Intervention. <https://repository.lib.ncsu.edu/bitstream/handle/1840.20/39743/etd.pdf?sequence=1>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_ :octicon:`graph;1em`
* `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_ :octicon:`comment-discussion;1em`
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the diffusion of test smells and their relationship with test code quality of Java projects <https://onlinelibrary.wiley.com/doi/abs/10.1002/smr.2532>`_ :octicon:`graph;1em`
* `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `On the influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the test smells detection: an empirical study on the jnose test accuracy <https://sol.sbc.org.br/journals/index.php/jserd/article/view/1893>`_ :octicon:`graph;1em`
* `On the use of test smells for prediction of flaky tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Pytest-Smell: a smell detection tool for Python unit tests <https://dl.acm.org/doi/10.1145/3533767.3543290>`_ :octicon:`graph;1em`
* `Refactoring Test Smells With JUnit 5: Why Should Developers Keep Up-to-Date? <https://ieeexplore.ieee.org/document/9769994/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_ :octicon:`file-code;1em` :octicon:`sync;1em`
* `Rule-based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Smart prediction for refactorings in the software test code <https://dl.acm.org/doi/10.1145/3474624.3477070>`_ :octicon:`graph;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `TEMPY: Test Smell Detector for Python <https://dl.acm.org/doi/10.1145/3555228.3555280>`_ :octicon:`graph;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `Test code quality and its relation to issue handling performance <https://ieeexplore.ieee.org/abstract/document/6862882/>`_ :octicon:`comment-discussion;1em`
* `TestAXE: Automatically Refactoring Test Smells Using JUnit 5 Features <https://sol.sbc.org.br/index.php/cbsoft_estendido/article/view/22311>`_ :octicon:`graph;1em` :octicon:`sync;1em`
* `The secret life of test smells-an empirical study on test smell evolution and maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `Toward static test flakiness prediction: a feasibility study <https://dl.acm.org/doi/10.1145/3472674.3473981>`_ :octicon:`graph;1em`
* `Understanding Testability and Test Smells <https://www.designite-tools.com/blog/understanding-testability-test-smells>`_
* `Understanding practitioners’ strategies to handle test smells: a multi-method study <https://dl.acm.org/doi/10.1145/3474624.3474639>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Unit Test Smells and Accuracy of Software Engineering Student Test Suites <https://dl.acm.org/doi/abs/10.1145/3430665.3456328?casa_token=igLWdXV-fTYAAAAA:UZiEPkDc2-NRE6_Zi0Q9FRDeUjeyZcdVTLO9Kzk53cVuo7LC-nC7m690pw6vZpQmMfa5ktOcw2pvFw>`_
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `tsDetect: an open source test smells detection tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
* `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
