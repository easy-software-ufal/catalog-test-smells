Redundant Print
^^^^^
Definitions:

* Print statements in unit tests are redundant as unit tests are executed as part of an automated. Furthermore, they can consume computing resources or increase execution time if the developer calls an intensive/long-running method from within the print method (i.e., as a parameter).


Code Example:

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

References:

 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

