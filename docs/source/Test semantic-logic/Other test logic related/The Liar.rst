The Liar
^^^^^
**Definition:**

* Testing asynchronous code becomes tricky as it is based on a future value that you might receive or might not.


**Code Example:**

.. code-block:: ruby

  test('the data is peanut butter', () => {
    function callback(data) {
      expect(data).toBe('peanut butter');
    }
    
    fetchData(callback);
  });


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `TDD anti patterns - Chapter 1 <https://www.codurance.com/publications/tdd-anti-patterns-chapter-1>`_ :octicon:`file-code;1em`
* `TDD anti-patterns - the liar, excessive setup, the giant, slow poke <https://marabesi.com/tdd/2021/08/28/tdd-anti-patterns.html>`_ :octicon:`file-code;1em`
* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Smells in Software Test Code: A Survey of Knowledge in Industry and Academia <https://www.sciencedirect.com/science/article/abs/pii/S0164121217303060>`_
* `Test-Driven Development: TDD Anti-Patterns <https://bryanwilhite.github.io/the-funky-knowledge-base/entry/kb2076072213/>`_
* `Unit Testing Anti-Patterns, Full List <https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html>`_

