The Stepford Fields
^^^^^
**Definition:**

* Where (too) many of the fields in test contain the same value, making it hard to spot when a calculation is reading a value from the wrong field, because it works on the test data; this also makes load testing near a cache pretty meaningless


**Code Example:**

.. code-block:: yaml

  name:
   title: Mr
   first: Testing
   last: Testing
  company: Testing

.. code-block:: 

  expect(person.getFullName())
    .toBe('Mr Testing Testing');
  expect(person.getCompanyName())
      .toBe('Testing');

  person.company = 'Testing';
  
  expect(person.getCompanyName())
    .toBe('Testing');


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_ :octicon:`file-code;1em`

