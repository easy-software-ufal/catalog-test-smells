Sensitive Equality
^^^^^
Definition:

* Occurs when the toString method is used within a test method. Test methods verify objects by invoking the default toString() method of the object and comparing the output against an specific string. Changes to the implementation of toString() might result in failure. The correct approach is to implement a custom method within the object to perform this comparison.


Also Known As:

* The Butterfly


Code Example:

.. code-block:: java

  @Test
  public void test1() throws UnknownHostException {

      String peersPacket = "F8 4E 11 F8 4B C5 36 81 " +
          "CC 0A 29 82 76 5F B8 40 D8 D6 0C 25 80 FA 79 5C " +
          "FC 03 13 EF DE BA 86 9D 21 94 E7 9E 7C B2 B5 22 " +
          "F7 82 FF A0 39 2C BB AB 8D 1B AC 30 12 08 B1 37 " +
          "E0 DE 49 98 33 4F 3B CF 73 FA 11 7E F2 13 F8 74 " +
          "17 08 9F EA F8 4C 21 B0";

      byte[] payload = Hex.decode(peersPacket);

      byte[] ip = decodeIP4Bytes(payload, 5);

      assertEquals(InetAddress.getByAddress(ip).toString(), ("/54.204.10.41"));
  }
      

References:

 * `Assessing Diffusion and Perception of Test Smells in Scala Projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `An Empirical Analysis of the Distribution of Unit Test Smells and Their Impact on Software Maintenance <https://ieeexplore.ieee.org/document/6405253>`_
 * `An Empirical Investigation Into the Nature of Test Smells <https://dl.acm.org/doi/10.1145/2970276.2970340>`_
 * `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_
 * `An Exploratory Study of the Relationship Between Software Test Smells and Fault-Proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_
 * `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
 * `Are Test Smells Really Harmful? An Empirical Study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_
 * `Developers Perception on the Severity of Test Smells: An Empirical Study <https://arxiv.org/abs/2107.13902>`_
 * `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
 * `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
 * `On the Diffusion of Test Smells in Automatically Generated Test Code: An Empirical Study <https://dl.acm.org/doi/10.1145/2897010.2897016>`_
 * `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
 * `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
 * `On the Interplay Between Software Testing and Evolution and Its Effect on Program Comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_
 * `On the Relation of Test Smells to Software Code Quality <https://ieeexplore.ieee.org/document/8529832>`_
 * `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_
 * `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_
 * `Scented Since the Beginning: On the Diffuseness of Test Smells in Automatically Generated Test Code <https://www.sciencedirect.com/science/article/pii/S0164121219301487?casa_token=UT0EMFzxTcQAAAAA:L9J82_15tdySkabcIMSHKPx8rVkrltOzcwgme5cIBWgT0txJENY5y-BdUmCYUoGHnoEjZJH-cYc>`_
 * `SoCRATES: Scala Radar for Test Smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
 * `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_
 * `Toward Static Test Flakiness Prediction: A Feasibility Study <https://dl.acm.org/doi/10.1145/3472674.3473981>`_
 * `Towards Automated Tools for Detecting Test Smells: An Empirical Investigation Into the Nature of Test Smells <https://dibt.unimol.it/staff/fpalomba/documents/C14.pdf>`_
 * `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_
 * `Why do builds fail?—A conceptual replication study <https://www.sciencedirect.com/science/article/pii/S0164121221000364>`_
 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

