Assertion Roulette
^^^^^
**Definition:**

* Occurs when a test method has multiple non-documented assertions. Multiple assertion statements in a test method without a descriptive message impacts readability/understandability/maintainability as it’s not possible to understand the reason for the failure of the test.


.. code-block:: python
    
    import unittest
 
    airLinesCode = ['2569','2450','2340']
    
    class Flight:
        def __init__(self,airLine,mileage):
            self.mileage = mileage
            self.airLine = airLine
            self.fullFuel = True
            
        def isValidAirLineCode(self):
            for airLineCode in airLinesCode:
                if(self.airLine == airLineCode):
                    return True
            return False

    class TestFlight(unittest.TestCase):
        def test_flight(self):
            flight = Flight('2569',1000)
            
            self.assertEqual(flight.mileage,1000)
            self.assertTrue(flight.fullFuel)
            self.assertTrue(flight.isValidAirLineCode())

    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Assessing Diffusion and Perception of Test Smells in Scala Projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_ :octicon:`file-code;1em`
* `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `Test Artifacts — The Practical Testing Book <https://damorimrg.github.io/practical_testing_book/goodpractices/artifacts.html>`_ :octicon:`file-code;1em`
* `A Survey on Test Practitioners' Awareness of Test Smells <https://arxiv.org/abs/2003.05613>`_
* `An Empirical Analysis of the Distribution of Unit Test Smells and Their Impact on Software Maintenance <https://ieeexplore.ieee.org/document/6405253>`_
* `An Empirical Investigation Into the Nature of Test Smells <https://dl.acm.org/doi/10.1145/2970276.2970340>`_
* `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_
* `An Exploratory Study of the Relationship Between Software Test Smells and Fault-Proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`graph;1em`
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
* `Are Test Smells Really Harmful? An Empirical Study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Developers Perception on the Severity of Test Smells: An Empirical Study <https://arxiv.org/abs/2107.13902>`_ :octicon:`graph;1em`
* `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_ :octicon:`graph;1em`
* `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `On the Diffusion of Test Smells in Automatically Generated Test Code: An Empirical Study <https://dl.acm.org/doi/10.1145/2897010.2897016>`_
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`graph;1em`
* `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the Interplay Between Software Testing and Evolution and Its Effect on Program Comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
* `On the Relation of Test Smells to Software Code Quality <https://ieeexplore.ieee.org/document/8529832>`_
* `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Pizza versus Pinsa: On the Perception and Measurability of Unit Test Code Quality <https://ieeexplore.ieee.org/document/9240623/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Quality defects detection in unit tests <https://jrnl.nau.edu.ua/index.php/IPZ/article/download/3084/3036/0>`_ :octicon:`comment-discussion;1em`
* `RAIDE: a tool for Assertion Roulette and Duplicate Assert identification and refactoring <https://dl.acm.org/doi/10.1145/3422392.3422510>`_ :octicon:`comment-discussion;1em`
* `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em`
* `Scented Since the Beginning: On the Diffuseness of Test Smells in Automatically Generated Test Code <https://www.sciencedirect.com/science/article/pii/S0164121219301487?casa_token=UT0EMFzxTcQAAAAA:L9J82_15tdySkabcIMSHKPx8rVkrltOzcwgme5cIBWgT0txJENY5y-BdUmCYUoGHnoEjZJH-cYc>`_
* `Smart Prediction for Refactorings in the Software Test Code <https://dl.acm.org/doi/10.1145/3474624.3477070>`_
* `SoCRATES: Scala Radar for Test Smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `Test-Related Factors and Post-release Defects: An Empirical Study <https://dl.acm.org/doi/10.1145/3338906.3342500>`_
* `TestQ: Exploring Structural and Maintenance Characteristics of Unit Test Suites <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.6409&rep=rep1&type=pdf>`_
* `The Relation of Test-Related Factors to Software Quality: A Case Study on Apache Systems <https://search.proquest.com/openview/c52d821a4dd6ecb046957d9d6a532ae0/1?pq-origsite=gscholar&cbl=326341>`_ :octicon:`graph;1em`
* `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `Toward Static Test Flakiness Prediction: A Feasibility Study <https://dl.acm.org/doi/10.1145/3472674.3473981>`_
* `Towards Automated Tools for Detecting Test Smells: An Empirical Investigation Into the Nature of Test Smells <https://dibt.unimol.it/staff/fpalomba/documents/C14.pdf>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
* `Unit Test Smells and Accuracy of Software Engineering Student Test Suites <https://dl.acm.org/doi/abs/10.1145/3430665.3456328?casa_token=igLWdXV-fTYAAAAA:UZiEPkDc2-NRE6_Zi0Q9FRDeUjeyZcdVTLO9Kzk53cVuo7LC-nC7m690pw6vZpQmMfa5ktOcw2pvFw>`_
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`graph;1em`
* `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_
* `Why do builds fail?—A conceptual replication study <https://www.sciencedirect.com/science/article/pii/S0164121221000364>`_
* `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`comment-discussion;1em`

