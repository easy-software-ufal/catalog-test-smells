Mystery Guest
^^^^^
Definition:

* A test case that uses external resources that are not managed by a fixture. A drawback of this approach is that the interface to external resources might change over time necessitating an update of the test case, or that those resources might not be available when the test case is run, endangering the deterministic behavior of the test.

Code Example:

.. code-block:: java

  public void testGetFlightsByFromAirport_OneOutboundFlight_mg() throws Exception {
      loadAirportsAndFlightsFromFile("test-flights.csv");
      // Exercise System
      List flightsAtOrigin = facade.getFlightsByOriginAirportCode( "YYC");
      // Verify Outcome
      assertEquals( 1, flightsAtOrigin.size());
      FlightDto firstFlight = (FlightDto) flightsAtOrigin.get(0);
      assertEquals( "Calgary", firstFlight.getOriginCity());
   }

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Let’s not <https://thoughtbot.com/blog/lets-not>`_
 * `Mystery Guest <https://thoughtbot.com/blog/mystery-guest>`_
 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

