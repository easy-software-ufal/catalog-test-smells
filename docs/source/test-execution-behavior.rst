Test execution/behavior
========================

Other test execution / behavior
--------------------
Chatty logging 
^^^^^
Definitions:

* Often a substitute for self-explanatory assertions or well defined test names, the test writes lots of data to the console or logs in order to explain test failures outside of the assertions

Also Known As:

*

Code Example::


References:
  * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`

Performance
--------------
Asynchronous Test
^^^^^^
Definitions:

* A few tests take inordinately long to run; those tests contain explicit delays.

Also Known As:

*

Code Example::
  def fool():
    #this is a code example
    pass

References:
  * xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>
