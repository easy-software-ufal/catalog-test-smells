Long Test
^^^^^
Definitions:

* A Long Test is a test that consists of lot of code and statements. Such tests are mostly (but not necessarily) complex and badly document the purpose of the test and the application code. Furthermore they tend to test too much functionality, maybe even getting eager.


Code Example:

.. code-block:: javascript

    // Subject under test
    function Stack () {
    this.items = []
    }
    Stack.prototype.push = function (item) { this.items.push(item) }
    Stack.prototype.pop = function () { return this.items.pop() }
    Stack.prototype.peek = function () { return this.items[this.items.length - 1] }
    Stack.prototype.depth = function () { return this.items.length }

    // Test
    module.exports = {
        makeSureEverythingWorks: function () {
            var subject = new Stack()

            // Test Push
            subject.push('A')
            subject.push('B')
            subject.push('C')

            assert.equal(subject.pop(), 'C')
            assert.equal(subject.pop(), 'B')
            assert.equal(subject.pop(), 'A')

            // Test Peek
            subject.push('D')
            subject.push('E')

            assert.equal(subject.peek(), 'E')

            subject.pop()

            assert.equal(subject.peek(), 'D')

            subject.pop()

            // Test Depth
            subject.push('F')
            subject.push('G')

            assert.equal(subject.depth(), 2)

            // Test Pop
            subject.pop()
            subject.pop()

            assert.equal(subject.depth(), 0)
            assert.equal(subject.pop(), undefined)
        }
    }

References:

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_
 * `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_

