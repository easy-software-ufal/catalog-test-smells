Flexible Test
^^^^^
**Definition:**

* Test code verifies different functionality depending on when or where it is run.


**Code Example:**

.. code-block:: java

  public void testDisplayCurrentTime_whenever() {
    // fixture setup
    TimeDisplay sut = new TimeDisplay();

    // exercise SUT
    String result = sut.getCurrentTimeAsHtmlFragment();

    // verify outcome
    Calendar time = new DefaultTimeProvider().getTime();
    StringBuffer expectedTime = new StringBuffer();
    expectedTime.append("<span class=\"tinyBoldText\">");

    if ((time.get(Calendar.HOUR_OF_DAY) == 0)
    && (time.get(Calendar.MINUTE) <= 1)) {
      expectedTime.append( "Midnight");
    } else if ((time.get(Calendar.HOUR_OF_DAY) == 12)
      && (time.get(Calendar.MINUTE) == 0)) { // noon
      expectedTime.append("Noon");
    } else {
      SimpleDateFormat fr = new SimpleDateFormat("h:mm a");
      expectedTime.append(fr.format(time.getTime()));
    }
    expectedTime.append("</span>");
    assertEquals( expectedTime, result);
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
