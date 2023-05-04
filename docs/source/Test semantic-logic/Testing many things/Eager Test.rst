Eager Test
^^^^^
Definitions:

* A test case that checks or uses more than one method of the class under test. Since its introduction, this smell has been somewhat broadly defined. It is left to interpretation which method calls count towards the maximum. Either all methods invoked on the class under test could count, or only the methods invoked on the same instance under test, or only the methods of which the return value is eventually used within an assertion.


Also Known As:

* The Test It All, Split Personality

Code Example:

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

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_
 * `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_
 * `Smells in software test code: A survey of knowledge in industry and academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

