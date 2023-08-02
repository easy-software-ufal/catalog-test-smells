General Fixture
^^^^^
**Definition:**

* Occurs when a test case fixture is too general and the test methods only access part of it. A test setup/fixture method that initializes fields that are not accessed by test methods indicates that the fixture is too generalized. A drawback of it being too general is that unnecessary work is being done when a test method is run.


**Code Example:**

.. code-block:: java

  public void testGetFlightsByFromAirport_OneOutboundFlight() throws Exception {
        setupStandardAirportsAndFlights();
        FlightDto outboundFlight = findOneOutboundFlight();
        // Exercise System
        List flightsAtOrigin = facade.getFlightsByOriginAirport(
                      outboundFlight.getOriginAirportId());
        // Verify Outcome
        assertOnly1FlightInDtoList( "Flights at origin", outboundFlight,
                                    flightsAtOrigin);
    }
    
    public void testGetFlightsByFromAirport_TwoOutboundFlights() throws Exception {
        setupStandardAirportsAndFlights();
        FlightDto[] outboundFlights = findTwoOutboundFlightsFromOneAirport();
        // Exercise System
        List flightsAtOrigin = facade.getFlightsByOriginAirport(
                      outboundFlights[0].getOriginAirportId());
        // Verify Outcome
        assertExactly2FlightsInDtoList( "Flights at origin", outboundFlights,
                                        flightsAtOrigin);
    }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A preliminary evaluation on the relationship among architectural and test smells <https://ieeexplore.ieee.org/document/10006864/>`_
* `A survey on test practitioners' awareness of test smells <https://arxiv.org/abs/2003.05613>`_
* `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_ :octicon:`graph;1em`
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `An analysis of information needs to detect test smells <https://www2.swc.rwth-aachen.de/docs/teaching/seminar2016/FsSE%20CTRelEng%202016.pdf#page=23>`_ :octicon:`comment-discussion;1em`
* `An empirical investigation into the nature of test smells <https://dl.acm.org/doi/10.1145/2970276.2970340>`_ :octicon:`sync;1em`
* `An exploratory study of the relationship between software test smells and fault-proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Are test smells really harmful? An empirical study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Automated Detection of Test Fixture Strategies and Smells <https://ieeexplore.ieee.org/document/6569744>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Automatic Identification of High-Impact Bug Report by Product and Test Code Quality <https://huang.zj.cn/pdf/J13.pdf>`_
* `Automatic Test Smell Detection Using Information Retrieval Techniques <https://ieeexplore.ieee.org/abstract/document/8530039>`_ :octicon:`graph;1em`
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`comment-discussion;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Characterizing High-Quality Test Methods: A First Empirical Study <https://ieeexplore.ieee.org/document/9796158/>`_ :octicon:`graph;1em`
* `Characterizing the Relative Significance of a Test Smell <https://ieeexplore.ieee.org/document/4021366>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Detecting redundant unit tests for AspectJ programs <https://ieeexplore.ieee.org/abstract/document/4021983>`_ :octicon:`comment-discussion;1em`
* `Enhancing developers’ awareness on test suites’ quality with test smell summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `How are test smells treated in the wild? A tale of two empirical studies <https://sol.sbc.org.br/journals/index.php/jserd/article/download/1802/1807/7485>`_ :octicon:`graph;1em`
* `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_ :octicon:`comment-discussion;1em`
* `Just-In-Time Test Smell Detection and Refactoring: The DARTS Project <https://fpalomba.github.io/pdf/Conferencs/C51.pdf>`_ :octicon:`sync;1em`
* `Let’s not <https://thoughtbot.com/blog/lets-not>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `On The Detection of Test Smells: A Metrics-Based Approach for General Fixture and Eager Test <https://ieeexplore.ieee.org/abstract/document/4359471>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the diffusion of test smells and their relationship with test code quality of Java projects <https://onlinelibrary.wiley.com/doi/abs/10.1002/smr.2532>`_ :octicon:`graph;1em`
* `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`graph;1em`
* `On the influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the interplay between software testing and evolution and its effect on program comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
* `On the test smells detection: an empirical study on the jnose test accuracy <https://sol.sbc.org.br/journals/index.php/jserd/article/view/1893>`_ :octicon:`graph;1em`
* `On the use of test smells for prediction of flaky tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `SoCRATES: Scala radar for test smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_ :octicon:`file-code;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `Strategies for avoiding text fixture smells during software evolution <https://ieeexplore.ieee.org/document/6624053>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
* `The secret life of test smells-an empirical study on test smell evolution and maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `Towards Automated Tools for Detecting Test Smells: An Empirical Investigation into the Nature of Test Smells <https://dibt.unimol.it/staff/fpalomba/documents/C14.pdf>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`graph;1em`
* `Why do builds fail?—A conceptual replication study <https://www.sciencedirect.com/science/article/pii/S0164121221000364>`_
* `tsDetect: an open source test smells detection tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
* `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
