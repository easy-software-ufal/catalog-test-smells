Evolve Or
^^^^^
**Definition:**

* Tests that are not maintained after SUT code evolution and still pass


**Code Example:**

.. code-block::

  public class TransactionTest {
    @Test
    public void shouldRecognizeTransactionsWithZeroValueAsInvalid() {
      //given
      Transaction tx = new Transaction(BigDecimal.ZERO,
      new InternalUser());
      //when
      boolean actual = tx.validate();
      //then
      assertThat(actual).isFalse();
    }
    
    @Test
    public void shouldRecognizeTransactionWithNegativeValueAsInvalid() {
      //given
      Transaction tx = new Transaction(BigDecimal.ONE.negate(),
      new InternalUser());
      //when
      boolean actual = tx.validate();
      //then
      assertThat(actual).isFalse();
    }
  }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
