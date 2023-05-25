Mystery Guest
^^^^^
**Definition:**

* A test case that uses external resources that are not managed by a fixture. A drawback of this approach is that the interface to external resources might change over time necessitating an update of the test case, or that those resources might not be available when the test case is run, endangering the deterministic behavior of the test.

**Code Example:**

.. code-block:: java

  public void testGetFlightsByFromAirport_OneOutboundFlight_mg() throws Exception {
      loadAirportsAndFlightsFromFile("test-flights.csv");
      // Exercise System
      List flightsAtOrigin = facade.getFlightsByOriginAirportCode( "YYC");
      // Verify Outcome
      assertEquals( 1, flightsAtOrigin.size());
      FlightDto firstFlight = (FlightDto) flightsAtOrigin.get(0);
      assertEquals( "Calgary", firstFlight.getOriginCity());
   }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A survey on test practitioners' awareness of test smells <https://arxiv.org/abs/2003.05613>`_
* `An empirical analysis of the distribution of unit test smells and their impact on software maintenance <https://ieeexplore.ieee.org/document/6405253>`_ :octicon:`graph;1em`
* `An empirical investigation into the nature of test smells <https://dl.acm.org/doi/10.1145/2970276.2970340>`_ :octicon:`sync;1em`
* `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_ :octicon:`graph;1em`
* `An exploratory study of the relationship between software test smells and fault-proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Are test smells really harmful? An empirical study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Detecting redundant unit tests for AspectJ programs <https://ieeexplore.ieee.org/abstract/document/4021983>`_
* `Enhancing developers’ awareness on test suites’ quality with test smell summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_ :octicon:`comment-discussion;1em`
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `Let’s not <https://thoughtbot.com/blog/lets-not>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Mystery Guest <https://thoughtbot.com/blog/mystery-guest>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `On the diffusion of test smells in automatically generated test code: an empirical study <https://dl.acm.org/doi/10.1145/2897010.2897016>`_
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`graph;1em`
* `On the influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the interplay between software testing and evolution and its effect on program comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
* `On the Relation of Test Smells to Software Code Quality <https://ieeexplore.ieee.org/document/8529832>`_
* `On the use of test smells for prediction of flaky tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Rails Testing Antipatterns <https://thoughtbot.com/upcase/videos/testing-antipatterns>`_ :octicon:`sync;1em`
* `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_ :octicon:`graph;1em`
* `Scented since the beginning: On the diffuseness of test smells in automatically generated test code <https://www.sciencedirect.com/science/article/pii/S0164121219301487?casa_token=UT0EMFzxTcQAAAAA:L9J82_15tdySkabcIMSHKPx8rVkrltOzcwgme5cIBWgT0txJENY5y-BdUmCYUoGHnoEjZJH-cYc>`_
* `SoCRATES: Scala radar for test smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
* `The Relation of Test-Related Factors to Software Quality: A Case Study on Apache Systems <https://search.proquest.com/openview/c52d821a4dd6ecb046957d9d6a532ae0/1?pq-origsite=gscholar&cbl=326341>`_ :octicon:`graph;1em`
* `The secret life of test smells-an empirical study on test smell evolution and maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `Toward static test flakiness prediction: a feasibility study <https://dl.acm.org/doi/10.1145/3472674.3473981>`_ :octicon:`graph;1em`
* `Towards Automated Tools for Detecting Test Smells: An Empirical Investigation into the Nature of Test Smells <https://dibt.unimol.it/staff/fpalomba/documents/C14.pdf>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `tsDetect: an open source test smells detection tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`graph;1em`
* `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_
* `Why do builds fail?—A conceptual replication study <https://www.sciencedirect.com/science/article/pii/S0164121221000364>`_
