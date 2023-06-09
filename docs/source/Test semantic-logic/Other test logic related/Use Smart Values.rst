Use Smart Values
^^^^^
**Definition:**

* Tests pass when the scenario they test is not really fulfilled

**Code Example:**

.. code-block:: java

  public class PriceCalculatorFactoryTest {
    SettingsService settings = mock(SettingsService.class);
    @Test
    public void shouldCreatePriceCalculator() {
      //given
      given(settings.getMinMargin()).willReturn(new BigDecimal(20));
      given(settings.getMaxMargin()).willReturn(new BigDecimal(50));
      given(settings.getPremiumShare()).willReturn(new BigDecimal(50));
      //when
      PriceCalculator calculator
      = new PriceCalculatorFactory(settings).create();
      Chapter 3. Strength
      7
      //then
      assertThat(calculator)
      .isEqualTo(new PriceCalculator(new BigDecimal(20),
      new BigDecimal(50), new BigDecimal(50)));
    }
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
