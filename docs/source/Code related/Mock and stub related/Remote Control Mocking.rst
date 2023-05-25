Remote Control Mocking
^^^^^
**Definition:**

* where a class that depends on a service is tested with those service’s complex dependencies mocked, rather than the service itself being mocked.


**Code Example:**


.. code-block:: pseudocode

  // pseudocode

  given: mock connection factory will return a mock connection
  given: mock connection, when queried will return a test collection
  given: repository with mock connection factory
  given: controller with repository
  when: controller handles a get request
  then: the result will be the test collection as json 

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`
