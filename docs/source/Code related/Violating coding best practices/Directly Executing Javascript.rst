Directly Executing Javascript
^^^^^
Definition:

* Since WebDriver can directly execute any arbitrary JavaScript, it can be tempting to bypass DOM manipulation and just run the JavaScript.


Code Example:

.. code-block:: java

  public void RemoveTea(string teaType)
  {
    (driver as IJavaScriptExecutor).ExecuteScript(string.Format(&quot;viewModel.tea.types.removeTeaType(\&quot;{0}\&quot;);&quot;, teaType));
  }

References:

 * `Five automated acceptance test anti-patterns <https://web.archive.org/web/20211113081220/https://alisterbscott.com/2015/01/20/five-automated-acceptance-test-anti-patterns/>`_



