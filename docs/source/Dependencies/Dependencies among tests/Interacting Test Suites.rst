Interacting Test Suites
^^^^^
Definitions:

* A special case of Interacting Tests where the tests are in different test suites.


Code Example:

.. code-block::

  Suite1.run()--> Green
  Suite2.run()--> Green
  Suite(Suite1,Suite2).run()--> Test C in Suite2 fails

References:

 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

