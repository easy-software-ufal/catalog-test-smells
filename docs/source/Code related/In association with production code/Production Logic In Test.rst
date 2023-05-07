Production Logic In Test
^^^^^
Definition:

* Some forms of Conditional Test Logic are found in the result verification section of our tests.


Code Example:

.. code-block:: java

 public void testCombinationsOfInputValues() {
    // Set up fixture
    Calculator sut = new Calculator();
    
    int expected; // TBD inside loops

    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        // Exercise SUT
        int actual = sut.calculate( i, j );
          
        // Verify result
        if (i==3 & j==4) // special case
          expected = 8;
        else
          expected = i+j;

        assertEquals(message(i,j), expected, actual);
      }
    }
  }

  private String message(int i, int j) {
    return "Cell( " + String.valueOf(i)+ ","
    + String.valueOf(j) + ")";
  }

References:

 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

