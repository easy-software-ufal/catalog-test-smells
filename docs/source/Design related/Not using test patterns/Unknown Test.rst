Unknown Test
^^^^^
Definitions:

* An assertion statement describes an expected condition for a test method. By examining the assertion statement, it is possible to understand the purpose of the test. However, It is possible for a test method to be written without an assertion statement, in such an instance JUnit will show the test method as passing if the  statements within the test method did not result in a thrown exception when executed.
* An assertion statement is used to declare an expected boolean condition for a test method. By examining the assertion statement it is possible to understand the purpose of the test method. However, It is possible for a test method to written sans an assertion statement, in such an instance JUnit will show the test method as passing if the statements within the test method did not result in an exception, when executed. New developers to the project will find it difficult in understanding the purpose of such test methods (more so if the name of the test method is not descriptive enough).
* An assertion statement describes an expected condition for a test method. By examining the assertion statement, it is possible to understand the purpose of the test. However, It is possible for a test method to be written without an assertion statement, in such an instance JUnit will show the test method as passing if the  statements within the test method did not result in a thrown exception when executed.


Code Example:

.. code-block:: java

  @Test
  public void hitGetPOICategoriesApi() throws Exception {
      POICategories poiCategories = apiClient.getPOICategories(16);
      for (POICategory category : poiCategories) {
        System.out.println(category.name() + ": " + category);
      }
  }

References:

 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

