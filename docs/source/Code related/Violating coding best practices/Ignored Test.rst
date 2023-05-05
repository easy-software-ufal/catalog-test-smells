Ignored Test
^^^^^
Definition:

* JUnit 4 provides developers with the ability to suppress test methods from running. However, these ignored test methods result in overhead since they add unnecessary overhead with regards to compilation time, and increases code complexity and comprehension.


Code Example:

.. code-block:: java

  @Ignore("disabled for now as this test is too flaky")
  public void peerPriority() throws Exception {
    final List addresses = Lists.newArrayList(
        new InetSocketAddress("localhost", 2000),
          new InetSocketAddress("localhost", 2001),
          new InetSocketAddress("localhost", 2002)
    );
      peerGroup.addConnectedEventListener(connectedListener);
      .....
  }
    

References:

 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

