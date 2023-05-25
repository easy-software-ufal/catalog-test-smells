Complex Assertions
^^^^^
**Definition:**

* The assertions in a test require many lines of code to implement. At first blush, since test-scoped logic is typically itself untested, this can be risky. Additionally, multi-line assertions are typically harder to read—both in terms of what they're doing and what they intend to say about the subject's behavior.


**Code Example:**

.. code-block:: javascript

  // Subject under test
  var _ = require('lodash')
  function incrementAge (people) {
    return _(_.cloneDeep(people)).map(function (person) {
      if (_.isNumber(person.age)) {
        person.age += 1
      }
      if (_.isArray(person.kids)) {
        person.kids = incrementAge(person.kids)
      }
      return person
    }).shuffle().value()
  }

  // Test
  module.exports = {
    incrementsSinglePersonAge: function () {
      var people = [
        {name: 'Jane', age: 39},
        {name: 'John', age: 99}
      ]
      var results = incrementAge(people)

      var jane = _.find(results, function (person) { return person.name === 'Jane' })
      assert.equal(jane.age, 40)
      var john = _.find(results, function (person) { return person.name === 'John' })
      assert.equal(john.age, 100)
    },
    incrementsKidsAgeToo: function () {
      var people = [
        {
          name: 'Joe',
          age: 42,
          kids: [
            {name: 'Jack', age: 8},
            {name: 'Jill', age: 7}
          ]}
      ]

      var results = incrementAge(people)

      var jack = _.find(results[0].kids, function (person) {
        return person.name === 'Jack'
      })
      assert.equal(jack.age, 9)
      var jill = _.find(results[0].kids, function (person) {
        return person.name === 'Jill'
      })
      assert.equal(jill.age, 8)
    }
  }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
