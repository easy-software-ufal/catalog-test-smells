Unrepeatable Test
^^^^^
Definition:

* A test behaves differently the first time it is run than how it behaves on subsequent test runs.


Code Example:

.. code-block:: smalltalk

  Suite.run()--> Green
  Suite.run()--> Test C fails
  Suite.run()--> Test C fails
  # User resets something
  Suite.run()--> Green
  Suite.run()--> Test C fails
  Suite.run()--> Test C fails

References:

 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_

