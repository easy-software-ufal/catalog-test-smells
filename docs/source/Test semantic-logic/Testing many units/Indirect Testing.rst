Indirect Testing
^^^^^
Definition:

* The Test Method is interacting with the SUT indirectly via another object thereby making the interactions more complex.


Code Example:

.. code-block:: java

   private final int LEGAL_CONN_MINS_SAME = 30;
   public void testAnalyze_sameAirline_LessThanConnectionLimit()
   throws Exception {
      // setup
      FlightConnection illegalConn = createSameAirlineConn( LEGAL_CONN_MINS_SAME - 1);
      // exercise
      FlightConnectionAnalyzerImpl sut = new FlightConnectionAnalyzerImpl();
      String actualHtml = sut.getFlightConnectionAsHtmlFragment( illegalConn.getInboundFlightNumber(),
                       illegalConn.getOutboundFlightNumber());
      // verification
      StringBuffer expected = new StringBuffer();
      expected.append("<span class=”boldRedText”>");
      expected.append("Connection time between flight ");
      expected.append(illegalConn.getInboundFlightNumber());
      expected.append(" and flight ");
      expected.append(illegalConn.getOutboundFlightNumber());
      expected.append(" is ");
      expected.append(illegalConn.getActualConnectionTime());
      expected.append(" minutes.</span>");
      assertEquals("html", expected.toString(), actualHtml);
   }

References:

 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_

