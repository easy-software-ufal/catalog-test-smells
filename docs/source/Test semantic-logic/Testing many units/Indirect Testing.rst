Indirect Testing
^^^^^
**Definition:**

* The Test Method is interacting with the SUT indirectly via another object thereby making the interactions more complex.


**Code Example:**

.. code-block:: java

   private final int LEGAL_CONN_MINS_SAME = 30;
   public void testAnalyze_sameAirline_LessThanConnectionLimit()
   throws Exception {
      // setup
      FlightConnection illegalConn = createSameAirlineConn( LEGAL_CONN_MINS_SAME - 1);
      // exercise
      FlightConnectionAnalyzerImpl sut = new FlightConnectionAnalyzerImpl();
      String actualHtml = sut.getFlightConnectionAsHtmlFragment( illegalConn.getInboundFlightNumber(),
                       illegalConn.getOutboundFlightNumber());
      // verification
      StringBuffer expected = new StringBuffer();
      expected.append("<span class=”boldRedText”>");
      expected.append("Connection time between flight ");
      expected.append(illegalConn.getInboundFlightNumber());
      expected.append(" and flight ");
      expected.append(illegalConn.getOutboundFlightNumber());
      expected.append(" is ");
      expected.append(illegalConn.getActualConnectionTime());
      expected.append(" minutes.</span>");
      assertEquals("html", expected.toString(), actualHtml);
   }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A survey on test practitioners' awareness of test smells <https://arxiv.org/abs/2003.05613>`_
* `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_ :octicon:`graph;1em`
* `An empirical analysis of the distribution of unit test smells and their impact on software maintenance <https://ieeexplore.ieee.org/document/6405253>`_ :octicon:`graph;1em`
* `An exploratory study of the relationship between software test smells and fault-proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Are test smells really harmful? An empirical study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Detecting redundant unit tests for AspectJ programs <https://ieeexplore.ieee.org/abstract/document/4021983>`_
* `Enhancing developers’ awareness on test suites’ quality with test smell summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `How are test smells treated in the wild? A tale of two empirical studies <https://sol.sbc.org.br/journals/index.php/jserd/article/download/1802/1807/7485>`_ :octicon:`graph;1em`
* `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `On the Relation of Test Smells to Software Code Quality <https://ieeexplore.ieee.org/document/8529832>`_
* `On the diffusion of test smells in automatically generated test code: an empirical study <https://dl.acm.org/doi/10.1145/2897010.2897016>`_
* `On the interplay between software testing and evolution and its effect on program comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
* `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_ :octicon:`graph;1em`
* `Scented since the beginning: On the diffuseness of test smells in automatically generated test code <https://www.sciencedirect.com/science/article/pii/S0164121219301487?casa_token=UT0EMFzxTcQAAAAA:L9J82_15tdySkabcIMSHKPx8rVkrltOzcwgme5cIBWgT0txJENY5y-BdUmCYUoGHnoEjZJH-cYc>`_
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
* `The Relation of Test-Related Factors to Software Quality: A Case Study on Apache Systems <https://search.proquest.com/openview/c52d821a4dd6ecb046957d9d6a532ae0/1?pq-origsite=gscholar&cbl=326341>`_ :octicon:`graph;1em`
* `Why do builds fail?—A conceptual replication study <https://www.sciencedirect.com/science/article/pii/S0164121221000364>`_
