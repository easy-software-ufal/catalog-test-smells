Remote Control Mocking
^^^^^
Definition:

* where a class that depends on a service is tested with those service’s complex dependencies mocked, rather than the service itself being mocked.


Code Example:


.. code-block:: pseudocode

  // pseudocode

  given: mock connection factory will return a mock connection
  given: mock connection, when queried will return a test collection
  given: repository with mock connection factory
  given: controller with repository
  when: controller handles a get request
  then: the result will be the test collection as json 

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

