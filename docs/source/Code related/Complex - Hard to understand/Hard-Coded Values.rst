Hard-Coded Values
^^^^^
Definitions:

* Scalar values or value objects that are used directly in fixture setup, as parameters in the test exercise or as expected values in the verification. That is, they are not assigned to a named constant or variable.


Code Example:

.. code-block:: csharp

    public function testGetTranslationFileTimestamp()
    {
        $this->fileManagerMock->expects($this->once())
            ->method('getTranslationFileTimestamp')
            ->willReturn(1445736974);
        $this->assertEquals(1445736974, $this->model->getTranslationFileTimestamp());
    }

References:

 * `Test Smell: Hard Coded Values <https://www.integer-net.com/test-smell-hard-coded-values/>`_

