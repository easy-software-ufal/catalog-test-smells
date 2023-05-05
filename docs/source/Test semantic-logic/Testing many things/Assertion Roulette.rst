Assertion Roulette
^^^^^
Definition:

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

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `Test Artifacts — The Practical Testing Book <https://damorimrg.github.io/practical_testing_book/goodpractices/artifacts.html>`_

