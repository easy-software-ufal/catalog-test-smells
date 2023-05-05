Code Pollution
^^^^^
Definition:

* It takes place when you introduce additional code to your main code base in order to enable unit testing


Code Example:

.. code-example:: java

    public interface ILogger
    {
        void Log(string text);
    }

    public class Logger : ILogger
    {
        public void Log(string text)
        {
            /* Log the text */
        }
    }

    public class FakeLogger : ILogger
    {
        public void Log(string text)
        {
        }
    }

    public class Controller
    {
        public void SomeMethod(ILogger logger)
        {
            logger.Log("SomeMethod is called");
        }
    }

References:

 * `Code pollution <https://enterprisecraftsmanship.com/posts/code-pollution/>`_

