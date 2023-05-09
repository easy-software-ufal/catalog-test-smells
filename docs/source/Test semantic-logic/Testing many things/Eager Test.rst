Eager Test
^^^^^
**Definition:**

* A test case that checks or uses more than one method of the class under test. Since its introduction, this smell has been somewhat broadly defined. It is left to interpretation which method calls count towards the maximum. Either all methods invoked on the class under test could count, or only the methods invoked on the same instance under test, or only the methods of which the return value is eventually used within an assertion.


**Also Known As:**

* The Test It All, Split Personality, Many Assertions, Multiple Assertions, The Free Ride

**Code Example:**

.. code-block:: java
    
   public void testFlightMileage_asKm2() throws Exception {
        // setup fixture
        // exercise contructor
        Flight newFlight = new Flight(validFlightNumber);
        // verify constructed object
        assertEquals(validFlightNumber, newFlight.number);
        assertEquals("", newFlight.airlineCode);
        assertNull(newFlight.airline);
        // setup mileage
        newFlight.setMileage(1122);
        // exercise mileage translater
        int actualKilometres = newFlight.getMileageAsKm();    
        // verify results
        int expectedKilometres = 1810;
        assertEquals( expectedKilometres, actualKilometres);
        // now try it with a canceled flight:
        newFlight.cancel();
        try {
            newFlight.getMileageAsKm();
            fail("Expected exception");
        } catch (InvalidRequestException e) {
            assertEquals( "Cannot get cancelled flight mileage", e.getMessage());
        }
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Assessing Diffusion and Perception of Test Smells in Scala Projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_  :octicon:`file-code;1em` :octicon:`graph;1em`
* `Smells in Software Test Code: A Survey of Knowledge in Industry and Academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_ :octicon:`file-code;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_  :octicon:`file-code;1em`
* `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `A Survey on Test Practitioners' Awareness of Test Smells <https://arxiv.org/abs/2003.05613>`_
* `An Analysis of Information Needs to Detect Test Smells <https://www2.swc.rwth-aachen.de/docs/teaching/seminar2016/FsSE%20CTRelEng%202016.pdf#page=23>`_ :octicon:`comment-discussion;1em`
* `An Empirical Analysis of the Distribution of Unit Test Smells and Their Impact on Software Maintenance <https://ieeexplore.ieee.org/document/6405253>`_
* `An Empirical Investigation Into the Nature of Test Smells <https://dl.acm.org/doi/10.1145/2970276.2970340>`_
* `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_
* `An Exploratory Study of the Relationship Between Software Test Smells and Fault-Proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`graph;1em`
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
* `Are Test Smells Really Harmful? An Empirical Study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Automatic Test Smell Detection Using Information Retrieval Techniques <https://ieeexplore.ieee.org/abstract/document/8530039>`_ :octicon:`graph;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Characterizing the Relative Significance of a Test Smell <https://ieeexplore.ieee.org/document/4021366>`_
* `Detecting Redundant Unit Tests for AspectJ Programs <https://ieeexplore.ieee.org/abstract/document/4021983>`_ :octicon:`comment-discussion;1em`
* `Developers Perception on the Severity of Test Smells: An Empirical Study <https://arxiv.org/abs/2107.13902>`_ :octicon:`graph;1em`
* `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `Just-In-Time Test Smell Detection and Refactoring: The DARTS Project <https://fpalomba.github.io/pdf/Conferencs/C51.pdf>`_
* `On The Detection of Test Smells: A Metrics-Based Approach for General Fixture and Eager Test <https://ieeexplore.ieee.org/abstract/document/4359471>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `On the Diffusion of Test Smells in Automatically Generated Test Code: An Empirical Study <https://dl.acm.org/doi/10.1145/2897010.2897016>`_
* `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`graph;1em`
* `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the Interplay Between Software Testing and Evolution and Its Effect on Program Comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
* `On the Relation of Test Smells to Software Code Quality <https://ieeexplore.ieee.org/document/8529832>`_
* `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Pizza versus Pinsa: On the Perception and Measurability of Unit Test Code Quality <https://ieeexplore.ieee.org/document/9240623/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em`
* `Rule-Based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Scented Since the Beginning: On the Diffuseness of Test Smells in Automatically Generated Test Code <https://www.sciencedirect.com/science/article/pii/S0164121219301487?casa_token=UT0EMFzxTcQAAAAA:L9J82_15tdySkabcIMSHKPx8rVkrltOzcwgme5cIBWgT0txJENY5y-BdUmCYUoGHnoEjZJH-cYc>`_
* `Smart Prediction for Refactorings in the Software Test Code <https://dl.acm.org/doi/10.1145/3474624.3477070>`_
* `SoCRATES: Scala Radar for Test Smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
* `Test Code Quality and Its Relation to Issue Handling Performance <https://ieeexplore.ieee.org/abstract/document/6862882/>`_ :octicon:`comment-discussion;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `Test-Related Factors and Post-release Defects: An Empirical Study <https://dl.acm.org/doi/10.1145/3338906.3342500>`_
* `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
* `The Relation of Test-Related Factors to Software Quality: A Case Study on Apache Systems <https://search.proquest.com/openview/c52d821a4dd6ecb046957d9d6a532ae0/1?pq-origsite=gscholar&cbl=326341>`_ :octicon:`graph;1em`
* `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `Toward Static Test Flakiness Prediction: A Feasibility Study <https://dl.acm.org/doi/10.1145/3472674.3473981>`_ :octicon:`graph;1em`
* `Towards Automated Tools for Detecting Test Smells: An Empirical Investigation Into the Nature of Test Smells <https://dibt.unimol.it/staff/fpalomba/documents/C14.pdf>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
* `Unit Test Smells and Accuracy of Software Engineering Student Test Suites <https://dl.acm.org/doi/abs/10.1145/3430665.3456328?casa_token=igLWdXV-fTYAAAAA:UZiEPkDc2-NRE6_Zi0Q9FRDeUjeyZcdVTLO9Kzk53cVuo7LC-nC7m690pw6vZpQmMfa5ktOcw2pvFw>`_
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`graph;1em`
* `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_

