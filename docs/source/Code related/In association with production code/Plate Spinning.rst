Plate Spinning
^^^^^
Definition:

* A test that is at risk of exiting prematurely because it does not properly wait for the results of external calls.


Code Example:

.. code-block:: javascript

  // Subject under test
  function download (path, cb) {
    get(path, function (er, value) {
      if (er) return cb(er)
      insert(value.id, value, function (er) {
        cb(er)
      })
    })
  }

  // Test
  module.exports = {
    beforeEach: function () {
      post('/interests', {id: 42, interests: ['Ruby on Rails']}, function () {})
    },
    getsAndThenInserts: function (done) {
      download('/interests', function (er) {
        select(42, function (er, value) {
          assert.deepEqual(value, {id: 42, interests: ['Ruby on Rails']})
          done(er)
        })
      })
    }
  }

  // Fake production implementations to simplify example test of subject
  var _ = require('lodash')
  var resources = {}
  function post (path, value, cb) {
    randomTimeout(function () {
      resources[path] = value
      cb(null)
    }, 10, 30)
  }

  function get (path, cb) {
    randomTimeout(function () {
      cb(null, resources[path])
    }, 15, 50)
  }

  var db = {}
  function insert (id, value, cb) {
    randomTimeout(function () {
      db[id] = value
      cb(null)
    })
  }

  function select (id, cb) {
    randomTimeout(function () {
      cb(null, db[id])
    })
  }

  function randomTimeout (func, low, high) {
    setTimeout(func, _(low || 10).range(high || 100).sample())
  }

  // Exclude this test from CI, since it's erratic
  if (process.env.CI) module.exports = {}

References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em`

