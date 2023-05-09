Test Code Duplication
^^^^^
Definition:


* This test smell normally identifies classes that contain test methods with repeated test code steps.


Code Example:

.. code-block:: python

    class TestFlight(unittest.TestCase):
        def test_mileage_init(self):
            airLine = '2569'
            mileage = 1000
            flight = Flight(airLine,mileage)
            self.assertEqual(flight.mileage,1000)
            
        def test_fuel_is_full(self):
            airLine = '2569'
            mileage = 1000
            flight = Flight(airLine,mileage)
            self.assertTrue(flight.fullFuel)
            
        def test_is_valid_air_line_code(self):
            airLine = '2569'
            mileage = 1000
            flight = Flight(airLine,mileage)
            self.assertTrue(flight.isValidAirLineCode())

    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)

References:

 * `LCCSS: A Similarity Metric for Identifying Similar Test Code <https://dl.acm.org/doi/10.1145/3425269.3425283>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_ :octicon:`file-code;1em`
 * `Test Artifacts — The Practical Testing Book <https://damorimrg.github.io/practical_testing_book/goodpractices/artifacts.html>`_ :octicon:`file-code;1em`
 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `A Survey on Test Practitioners' Awareness of Test Smells <https://arxiv.org/abs/2003.05613>`_
 * `An Empirical Analysis of the Distribution of Unit Test Smells and Their Impact on Software Maintenance <https://ieeexplore.ieee.org/document/6405253>`_
 * `An Exploratory Study of the Relationship Between Software Test Smells and Fault-Proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`graph;1em`
 * `Are Test Smells Really Harmful? An Empirical Study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
 * `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_ :octicon:`comment-discussion;1em`
 * `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
 * `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
 * `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_ :octicon:`graph;1em`
 * `On the Diffusion of Test Smells in Automatically Generated Test Code: An Empirical Study <https://dl.acm.org/doi/10.1145/2897010.2897016>`_
 * `On the Interplay Between Software Testing and Evolution and Its Effect on Program Comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
 * `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em`
 * `Test Code Quality and Its Relation to Issue Handling Performance <https://ieeexplore.ieee.org/abstract/document/6862882/>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_

