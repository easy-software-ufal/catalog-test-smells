Conditional Verification Logic
^^^^^
Definition:

* This is usually caused by wanting to prevent the execution of assertions if the SUT fails to return the right objects or the use of loops to verify the contents of collections returned by the SUT.


Code Example:

.. code-block:: java

  public void testCombinationsOfInputValues() {
    Calculator sut = new Calculator();
    int expected;

    for (int i = 0; i < 10; i++){
      for(int j = 0 ; j < 10; j++){
        int acutal = sut.calculate(i , j);

        if(i==3 & j==4){
          expected = 8;
        } else {
          expected = i+j;
        }

        assertEquals(message(i, j), expected, actual);
      }
    }
  }

  private String message(int i, int j) {
    return "Cell (" + String.valueOf(i) + ", " + String.valueOf(j) + ")";
  }

References:

 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

