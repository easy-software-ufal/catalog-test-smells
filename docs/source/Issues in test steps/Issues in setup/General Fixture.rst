General Fixture
^^^^^
Definition:

* Occurs when a test case fixture is too general and the test methods only access part of it. A test setup/fixture method that initializes fields that are not accessed by test methods indicates that the fixture is too generalized. A drawback of it being too general is that unnecessary work is being done when a test method is run.


Code Example:

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

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Let’s not <https://thoughtbot.com/blog/lets-not>`_
 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_
 * `SoCRATES: Scala radar for test smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

