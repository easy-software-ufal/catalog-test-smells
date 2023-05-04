Lazy Test
^^^^^
Definitions:

* More than one test case with the same fixture that tests the same method. This smell affects test maintainability, as assertions testing the same method should be in the same test case. Like EAGER TEST, the original definition [3] leaves some details to interpretation. We consider every call to the class under test as a potential cause of LAZY TEST, irrespective of whether their results are used in an assertion.


Code Example:

.. code-block:: java

  @Test
  public void testDecrypt() throws Exception {
      FileInputStream file = new FileInputStream(ENCRYPTED_DATA_FILE_4_14);
      byte[] enfileData = new byte[file.available()];
      FileInputStream input = new FileInputStream(DECRYPTED_DATA_FILE_4_14);
      byte[] fileData = new byte[input.available()];
      input.read(fileData);
      input.close();
      file.read(enfileData);
      file.close();
      String expectedResult = new String(fileData, "UTF-8");
      assertEquals("Testing simple decrypt",expectedResult, Cryptographer.decrypt(enfileData, "test"));
  }

  @Test
  public void testEncrypt() throws Exception {
      String xml = readFileAsString(DECRYPTED_DATA_FILE_4_14);
      byte[] encrypted = Cryptographer.encrypt(xml, "test");
      String decrypt = Cryptographer.decrypt(encrypted, "test");
      assertEquals(xml, decrypt);
  }

References:

 * `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

