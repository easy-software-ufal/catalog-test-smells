Asynchronous Test
^^^^^
Definitions:

* A few tests take inordinately long to run; those tests contain explicit delays.


Code Example:

.. code-block:: java

  public class RequestHandlerThreadTest extends TestCase {
    private static final int TWO_SECONDS = 3000;
    public void testWasInitialized_Async() throws InterruptedException {
      RequestHandlerThread sut = new RequestHandlerThread();

      sut.start();

      Thread.sleep(TWO_SECONDS);
      assertTrue(sut.initializedSuccessfully());
    }

    public void testHandleOneRequest_Async() throws InterruptedException {
      RequestHandlerThread sut = new RequestHandlerThread();
      sut.start();

      enqueueRequest(makeSimpleRequest());

      Thread.sleep(TWO_SECONDS);
      assertEquals(1, sut.getNumberOfRequestsCompleted());
      assertResponseEquals(makeSimpleResponse(), getResponse());
    }
  }

References:

 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

