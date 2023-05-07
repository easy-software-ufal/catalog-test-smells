Conditional Test Logic
^^^^^
Definition:

* Test methods need to be simple and execute all statements in the production method. Conditions within the test method will alter the behavior of the test and its expected output, and would lead to situations where the test fails to detect defects in the production method since test statements were not executed as a condition was not met. Furthermore, conditional code within a test method negatively impacts the ease of comprehension by developers.


Also Known As:

* Indented Test Code

Code Example:

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

References:

 * `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_
 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_
 * `A Survey on Test Practitioners' Awareness of Test Smells <https://arxiv.org/abs/2003.05613>`_
 * `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_
 * `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_
 * `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
 * `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_
 * `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_
 * `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_
 * `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
 * `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
 * `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_
 * `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_
 * `Smart Prediction for Refactorings in the Software Test Code <https://dl.acm.org/doi/10.1145/3474624.3477070>`_
 * `Test Code Quality and Its Relation to Issue Handling Performance <https://ieeexplore.ieee.org/abstract/document/6862882/>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_
 * `Toward Static Test Flakiness Prediction: A Feasibility Study <https://dl.acm.org/doi/10.1145/3472674.3473981>`_
 * `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
 * `Unit Test Smells and Accuracy of Software Engineering Student Test Suites <https://dl.acm.org/doi/abs/10.1145/3430665.3456328?casa_token=igLWdXV-fTYAAAAA:UZiEPkDc2-NRE6_Zi0Q9FRDeUjeyZcdVTLO9Kzk53cVuo7LC-nC7m690pw6vZpQmMfa5ktOcw2pvFw>`_

