Happy Path
^^^^^
**Definition:**

* A test that uses known input, which executes without exception and produces an expected output.


**Code Example:**

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


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Improving Student Testing Practices through a Lightweight Checklist Intervention. <https://repository.lib.ncsu.edu/bitstream/handle/1840.20/39743/etd.pdf?sequence=1>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Smells in software test code: A survey of knowledge in industry and academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_
* `Unit Testing Anti-Patterns, Full List <https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html>`_
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_
