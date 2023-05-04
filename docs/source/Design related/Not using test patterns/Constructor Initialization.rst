Constructor Initialization
^^^^^
Definitions:

* Ideally, the test suite should not have a constructor. Initialization of fields should be in the setUp() method. Developers who are unaware of the purpose of setUp() method would give rise to this smell by defining a constructor for the test suite.


Code Example:

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

References:

 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

