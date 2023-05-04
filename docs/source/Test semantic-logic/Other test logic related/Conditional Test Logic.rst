Conditional Test Logic
^^^^^
Definitions:

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

 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_
 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

