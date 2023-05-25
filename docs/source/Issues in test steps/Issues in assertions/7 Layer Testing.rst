7 Layer Testing
^^^^^
**Definition:**

* Numerous tests depend on the functionality of a single unit, typically incidentally. A single change in the code often breaks many tests in the build. Often exhibits itself when a team finds that even trivial changes to a system results in exorbitant effort to get back to a green build.


**Code Example:**

.. code-block:: javascript

  // Subject under test
  var _ = require('lodash')
  function annualProfit (year) {
    return _.sumBy(_.range(1, 13), function (month) {
      return monthlyProfit(year, month)
    })
  }

  function monthlyProfit (year, month) {
    return _.sumBy(_.range(1, 32), function (day) {
      return dailyProfit(year, month, day)
    })
  }

  function dailyProfit (year, month, day) {
    var transactions = repo.find({year: year, month: month, day: day})
    return _.sumBy(transactions, function (transaction) {
      return transactionProfit(transaction)
    })
  }

  function transactionProfit (transaction) {
    return Math.round(transaction.price - transaction.cost)
  }

  // Test
  module.exports = {
    computesAnnualProfit: function () {
      repo.saveTransactions([
        {year: 2016, month: 3, day: 14, price: 55.44, cost: 80.30},
        {year: 2016, month: 6, day: 20, price: 9.33, cost: 4.00},
        {year: 2016, month: 12, day: 31, price: 112.48, cost: 100.24},
        // Bad year:
        {year: 2015, month: 3, day: 14, price: 999, cost: 0}
      ])

      var result = annualProfit(2016)

      assert.equal(result, -8)
    },
    computesMonthlyProfit: function () {
      repo.saveTransactions([
        {year: 2016, month: 5, day: 1, price: 108.99, cost: 70.45},
        {year: 2016, month: 5, day: 15, price: 208.13, cost: 133.55},
        {year: 2016, month: 5, day: 31, price: 90.00, cost: 80.03},
        // Bad month:
        {year: 2016, month: 6, day: 14, price: 999, cost: 0}
      ])

      var result = monthlyProfit(2016, 5)

      assert.equal(result, 124)
    },
    computesDailyProfit: function () {
      repo.saveTransactions([
        {year: 2016, month: 5, day: 12, price: 19.44, cost: 18.11},
        {year: 2016, month: 5, day: 12, price: 21.40, cost: 22.01},
        {year: 2016, month: 5, day: 12, price: 998.10, cost: 907.20},
        // Bad day:
        {year: 2016, month: 5, day: 1, price: 999, cost: 0}
      ])

      var result = dailyProfit(2016, 5, 12)

      assert.equal(result, 91)
    },
    computesTransactionProfit: function () {
      var transaction = {price: 33.22, cost: 20.11}

      var result = transactionProfit(transaction)

      assert.equal(result, 13)
    },
    afterEach: function () {
      repo.reset()
    }
  }

  // Fake production implementations to simplify example test of subject
  var repo = {
    __transactions: [],
    reset: function () {
      repo.__transactions = []
    },
    saveTransactions: function (transactions) {
      repo.__transactions.push.apply(repo.__transactions, transactions)
    },
    find: function (criteria) {
      return _.filter(repo.__transactions, criteria)
    }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
