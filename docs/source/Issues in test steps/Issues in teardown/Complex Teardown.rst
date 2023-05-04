Complex Teardown
^^^^^
Definitions:

* Complex fixture teardown code is more likely to leave test environment corrupted by not cleaning up correctly. It is hard to verify that it has been written correctly and can easily result in "data leaks" that may later cause this or other tests to fail for no apparent reason.


Code Example:

.. code-block:: java
  
  public void testGetFlightsByOrigin_NoInboudFlight_SMRTD() throws exception{
    BigDecimal outboundAirport = createTestAirport("1OF");
    BigDecimal inboundAirport = null;
    FlightDto expFlightDto = null;

    try {
      inboundAirport = createTestAirport("1IF");
      expFlightDto = 
            createTestFlight(outboundAirport, inboundAirport);
      
      List flightsAtDestination1 =
            facade.getFlightsByOriginAirport(inboundAirport);
      
      assertEquals(0, flightsAtDestination1.size());
    } finally {
      try {
        facade.removeFlight(expFlightDto.getFlightNumber());
      } finally {
        try {
          facade.removeAirport(inboundAirport);
        }finally {
          facade.removeAirport(outboundAirport);
        }
      }
    }
  }


References:

 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

