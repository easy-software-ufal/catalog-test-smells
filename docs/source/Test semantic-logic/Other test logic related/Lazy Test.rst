Lazy Test
^^^^^
**Definition:**

* More than one test case with the same fixture that tests the same method. This smell affects test maintainability, as assertions testing the same method should be in the same test case. Like EAGER TEST, the original definition [3] leaves some details to interpretation. We consider every call to the class under test as a potential cause of LAZY TEST, irrespective of whether their results are used in an assertion.


**Code Example:**

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

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `An Empirical Study into the Relationship Between Class Features and Test Smells <https://ieeexplore.ieee.org/document/7890581>`_ :octicon:`graph;1em`
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `An empirical analysis of the distribution of unit test smells and their impact on software maintenance <https://ieeexplore.ieee.org/document/6405253>`_ :octicon:`graph;1em`
* `An exploratory study of the relationship between software test smells and fault-proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Are test smells really harmful? An empirical study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Assessing diffusion and perception of test smells in scala projects <https://dl.acm.org/doi/10.1109/MSR.2019.00072>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Automatic Identification of High-Impact Bug Report by Product and Test Code Quality <https://huang.zj.cn/pdf/J13.pdf>`_
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Developers perception on the severity of test smells: an empirical study <https://arxiv.org/abs/2107.13902>`_ :octicon:`graph;1em` :octicon:`sync;1em`
* `Enhancing developers’ awareness on test suites’ quality with test smell summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `On the diffusion of test smells and their relationship with test code quality of Java projects <https://onlinelibrary.wiley.com/doi/abs/10.1002/smr.2532>`_ :octicon:`graph;1em`
* `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`graph;1em`
* `On the influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the interplay between software testing and evolution and its effect on program comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
* `On the test smells detection: an empirical study on the jnose test accuracy <https://sol.sbc.org.br/journals/index.php/jserd/article/view/1893>`_ :octicon:`graph;1em`
* `On the use of test smells for prediction of flaky tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Refactoring Test Smells With JUnit 5: Why Should Developers Keep Up-to-Date? <https://ieeexplore.ieee.org/document/9769994/>`_
* `SoCRATES: Scala radar for test smells <https://dl.acm.org/doi/10.1145/3337932.3338815>`_
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `The secret life of test smells-an empirical study on test smell evolution and maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`graph;1em`
* `tsDetect: an open source test smells detection tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
