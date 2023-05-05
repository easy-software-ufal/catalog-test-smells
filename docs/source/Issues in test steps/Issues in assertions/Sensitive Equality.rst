Sensitive Equality
^^^^^
Definition:

* Occurs when the toString method is used within a test method. Test methods verify objects by invoking the default toString() method of the object and comparing the output against an specific string. Changes to the implementation of toString() might result in failure. The correct approach is to implement a custom method within the object to perform this comparison.


Code Example:

.. code-block:: java

  @Test
  public void test1() throws UnknownHostException {

      String peersPacket = "F8 4E 11 F8 4B C5 36 81 " +
          "CC 0A 29 82 76 5F B8 40 D8 D6 0C 25 80 FA 79 5C " +
          "FC 03 13 EF DE BA 86 9D 21 94 E7 9E 7C B2 B5 22 " +
          "F7 82 FF A0 39 2C BB AB 8D 1B AC 30 12 08 B1 37 " +
          "E0 DE 49 98 33 4F 3B CF 73 FA 11 7E F2 13 F8 74 " +
          "17 08 9F EA F8 4C 21 B0";

      byte[] payload = Hex.decode(peersPacket);

      byte[] ip = decodeIP4Bytes(payload, 5);

      assertEquals(InetAddress.getByAddress(ip).toString(), ("/54.204.10.41"));
  }
      

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

