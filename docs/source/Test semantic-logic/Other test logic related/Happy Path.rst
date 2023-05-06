Happy Path
^^^^^
Definition:

* A test that uses known input, which executes without exception and produces an expected output.


Code Example:

.. code-block::

  @Test
  public void shouldProcessPacket() throws IOException, ServletException {
    //given
    given(request.getParameter(PacketApi.PACKET_PARAMETER))
    .willReturn(PACKET);
    given(request.getParameter(PacketApi.TYPE_PARAMETER))
    .willReturn(TYPE);
    //when
    servlet.doGet(request, response);
    //then
    verify(packetDataProcessor).process(PACKET, TYPE);
  }


References:

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_
 * `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_
 * `Smells in software test code: A survey of knowledge in industry and academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_
 * `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_
 * `Unit Testing Anti-Patterns, Full List <https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html>`_

