Default Test
^^^^^
Definitions:

* By default Android Studio creates default test classes when a project is created. These template test classes are meant to serve as an example for developers when writing unit tests and should either be removed or renamed. Having such files in the project will cause developers to start adding test methods into these files, making the default test class a container of all test cases and violate good testing practices. Problems would also arise when the classes need to be renamed in the future.
* By default Android Studio creates default test classes when a project is created. These classes are meant to serve as an example for developers when wring unit tests and should either be removed or renamed. Having such files in the project will cause developers to start adding test methods into these files, making the default test class a container of all test cases. This also would possibly cause problems when the classes need to be renamed in the future.
* By default Android Studio creates default test classes when a project is created. These template test classes are meant to serve as an example for developers when writing unit tests and should either be removed or renamed. Having such files in the project will cause developers to start adding test methods into these files, making the default test class a container of all test cases and violate good testing practices. Problems would also arise when the classes need to be renamed in the future.


Code Example::

.. code-block:: java
public class ExampleUnitTest {
    @Test
	public void addition_isCorrect() throws Exception {
		assertEquals(4, 2 + 2);
	}

    @Test
    public void shareProblem() throws InterruptedException {
    	.....
		Observable.just(200)
 		.subscribeOn(Schedulers.newThread())
		.subscribe(begin.asAction());
		begin.set(200);
		Thread.sleep(1000);
		assertEquals(beginTime.get(), "200");
    	.....
	}
	.....
}
            
References:

 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

