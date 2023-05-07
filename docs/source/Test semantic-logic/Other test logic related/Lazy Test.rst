Lazy Test
^^^^^
Definition:

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

 * `Assessing Diffusion and Perception of Test Smells in Scala Projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `An Empirical Analysis of the Distribution of Unit Test Smells and Their Impact on Software Maintenance <https://ieeexplore.ieee.org/document/6405253>`_
 * `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_
 * `An Exploratory Study of the Relationship Between Software Test Smells and Fault-Proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_
 * `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
 * `Are Test Smells Really Harmful? An Empirical Study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_
 * `Developers Perception on the Severity of Test Smells: An Empirical Study <https://arxiv.org/abs/2107.13902>`_
 * `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
 * `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
 * `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_
 * `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
 * `On the Interplay Between Software Testing and Evolution and Its Effect on Program Comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_
 * `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_
 * `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_
 * `SoCRATES: Scala Radar for Test Smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_
 * `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

