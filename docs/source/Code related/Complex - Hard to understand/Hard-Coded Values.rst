Hard-Coded Values
^^^^^
**Definition:**

* Scalar values or value objects that are used directly in fixture setup, as parameters in the test exercise or as expected values in the verification. That is, they are not assigned to a named constant or variable.


**Code Example:**

.. code-block:: csharp

    public function testGetTranslationFileTimestamp()
    {
        $this->fileManagerMock->expects($this->once())
            ->method('getTranslationFileTimestamp')
            ->willReturn(1445736974);
        $this->assertEquals(1445736974, $this->model->getTranslationFileTimestamp());
    }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Hunting for smells in natural language tests <https://ieeexplore.ieee.org/abstract/document/6606682>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Test Smell: Hard Coded Values <https://www.integer-net.com/test-smell-hard-coded-values/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
