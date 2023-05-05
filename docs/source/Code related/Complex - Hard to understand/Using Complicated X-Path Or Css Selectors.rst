Using Complicated X-Path Or Css Selectors
^^^^^
Definitions:

* Using element identification selectors that have long chains from the DOM in them leads to fragile tests, as any change to that chain in the DOM will break your tests.


Code Example:

.. code-block:: java

  private static readonly By TeaTypeSelector =
            By.CssSelector(
                &quot;#input-tea-type &gt; div &gt; div.TeaSearchRow &gt; div.TeaSearchCell.no &gt; div:nth-child(2) &gt; label&quot;);

References:

 * `Five automated acceptance test anti-patterns <https://web.archive.org/web/20220627170939/https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns//>`_

