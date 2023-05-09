Equality Pollution
^^^^^
Definition:

* The code that is put into production contains logic that should be exercised only during tests… A system that behaves one way in the test lab and an entirely different way in production is a recipe for disaster!


Code Example:

.. code-block:: java

  /// <summary>
  /// Verifies that two objects are equal, using a default comparer.
  /// </summary>
  /// <typeparam name="T">The type of the objects to be compared</typeparam>
  /// <param name="expected">The expected value</param>
  /// <param name="actual">The value to be compared against</param>
  /// <exception cref="EqualException">Thrown when the objects are not equal</exception>
  public static void Equal<T>(T expected, T actual)
  {
      Equal(expected, actual, GetEqualityComparer<T>());
  }

References:

 * `How to Compare Object Instances in your Unit Tests Quickly and Easily <https://buildplease.com/pages/testing-deep-equalilty/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`comment-discussion;1em`

