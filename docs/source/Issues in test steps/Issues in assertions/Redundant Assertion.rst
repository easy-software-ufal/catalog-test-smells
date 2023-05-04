Redundant Assertion
^^^^^
Definitions:

* Extra calls to an assert method where the condition being tested is a hard coded true value.
* This smell occurs when test methods contain assertion statements that are either always true or always false. A test is intended to return a binary outcome of whether the intended result is correct or not, and should not return the same output regardless of the input.
* This smell is introduced by developers for debugging purposes and then forgotten.

Code Example:

.. code-block:: java

  @Test
  public void testTrue() {
      assertEquals(true, true);
  }

References:

 * `JUnit Anti-patterns <https://exubero.com/junit/anti-patterns/>`_
 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

