Constructor Initialization
^^^^^
**Definition:**

* Ideally, the test suite should not have a constructor. Initialization of fields should be in the setUp() method. Developers who are unaware of the purpose of setUp() method would give rise to this smell by defining a constructor for the test suite.


**Code Example:**

.. code-block:: java

	public class TagEncodingTest extends BrambleTestCase {
		private final CryptoComponent crypto;
		private final SecretKey tagKey;
		private final long streamNumber = 1234567890;

		public TagEncodingTest() {
			crypto = new CryptoComponentImpl(new TestSecureRandomProvider());
			tagKey = TestUtils.getSecretKey();
		}

		@Test
		public void testKeyAffectsTag() throws Exception {
			Set set = new HashSet<>();
			for (int i = 0; i < 100; i++) {
				byte[] tag = new byte[TAG_LENGTH];
				SecretKey tagKey = TestUtils.getSecretKey();
				crypto.encodeTag(tag, tagKey, PROTOCOL_VERSION, streamNumber);
				assertTrue(set.add(new Bytes(tag)));
			}
		}
	...
	}

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `A Survey on Test Practitioners' Awareness of Test Smells <https://arxiv.org/abs/2003.05613>`_
* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
* `Developers Perception on the Severity of Test Smells: An Empirical Study <https://arxiv.org/abs/2107.13902>`_ :octicon:`graph;1em`
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_

