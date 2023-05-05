Test Code Duplication
^^^^^
Definitions:


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

 * `LCCSS: A Similarity Metric for Identifying Similar Test Code <https://dl.acm.org/doi/10.1145/3425269.3425283>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Test Artifacts — The Practical Testing Book <https://damorimrg.github.io/practical_testing_book/goodpractices/artifacts.html>`_
 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

