Using Complicated X-Path Or Css Selectors
^^^^^
**Definition:**

* Using element identification selectors that have long chains from the DOM in them leads to fragile tests, as any change to that chain in the DOM will break your tests.


**Code Example:**

.. code-block:: java

  private static readonly By TeaTypeSelector =
            By.CssSelector(
                '#input-tea-type < div < div.TeaSearchRow < div.TeaSearchCell.no < div:nth-child(2) < label');

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Five automated acceptance test anti-patterns <https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_ :octicon:`file-code;1em`
