Issues in test steps
====================

Issues in assertions
--------------------

7 Layer Testing
^^^^^^^^^^^^^^^

Definitions:

* Numerous tests depend on the functionality of a single unit, typically incidentally. A single change in the code often breaks many tests in the build. Often exhibits itself when a team finds that even trivial changes to a system results in exorbitant effort to get back to a green build.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Asserting Pre-condition and Invariants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Using the same API to express pre-conditions (i.e. argument validation), post-conditions, invariants, and assertions.

Also Known As:

* 

Code Example::

References:
  * Parameterized Test Patterns For Effective Testing with Pex

Assertion diversion
^^^^^^^^^^^^^^^^^^^

Definitions:

* where the wrong sort of assert is used, thus making a test failure harder to understand

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Assertionless Test
^^^^^^^^^^^^^^^^^^

Definitions:

* A test that does not contain at least one valid assertion is not a real test as it does only execute plain source-code, but never assert any data, state or functionality.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Assertionless Test
^^^^^^^^^^^^^^^^^^

Definitions:

* Pretending to assert data and functionality, but does not

Also Known As:

* 

Code Example::

References:
  * Rule-based Assessment of Test Quality

Assertions should be Merciless
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests whose assertions do not prove the test method works correctly

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Brittle Test
^^^^^^^^^^^^

Definitions:

* UI tests containing procedural test code, duplicated steps and magic values

Also Known As:

* 

Code Example::

References:
  * Maintainable automated ui tests

Brittle UI Tests
^^^^^^^^^^^^^^^^

Definitions:

* Tests having fixed delays, bad selectors and targeting elements, and difficult investigating failures

Also Known As:

* 

Code Example::

References:
  * Tips to avoid brittle ui tests

Broad Assertion
^^^^^^^^^^^^^^^

Definitions:

* Assertions that do not compare exact content and are, therefore, broad

Also Known As:

* 

Code Example::

References:
  * Developer test anti-patterns by lasse koskela

Bumbling assertions
^^^^^^^^^^^^^^^^^^^

Definitions:

* where there was a more articulate assertion available, but we chose a less sophisticated one and kind of got the message across. E.g. testing exceptions the hard way, or using equality check on list size, rather than a list size assertion.

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Calculating expected results on the fly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Any automated test that performs a comparison needs to know the expected results. If you believe that automatically calculating expected results is for you then I would at least consider separating the code that calculates the expected results from the code that performs the actual test.

Also Known As:

* 

Code Example::

References:
  * How test automation with selenium can fail

Commented Test
^^^^^^^^^^^^^^

Definitions:

* Test contents are commented so that it passes

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Complex Assertions
^^^^^^^^^^^^^^^^^^

Definitions:

* The assertions in a test require many lines of code to implement. At first blush, since test-scoped logic is typically itself untested, this can be risky. Additionally, multi-line assertions are typically harder to read—both in terms of what they're doing and what they intend to say about the subject's behavior.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Conspiracy of silence
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When assertions in tests are failing with almost no clue why

Also Known As:

* 

Code Example::

References:
  * Anti-patterns in test automation

Fantasy Tests
^^^^^^^^^^^^^

Definitions:

* Passing tests of code that wouldn't actually work in production, usually as a result of a stub returning a response that's substantially different from how a real instance would behave.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Fragile Tests
^^^^^^^^^^^^^

Definitions:

* tests which seem to break when they shouldn't

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns

Fuzzy assertions
^^^^^^^^^^^^^^^^

Definitions:

* where lack of control for the system under test, causes us not to be able to predict the exact outcome, leading to fuzzy or partial matching in our assertions

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Inadequate Assertion
^^^^^^^^^^^^^^^^^^^^

Definitions:

* Every update to the execution state must eventually be verified in the assertions. In principle, assertions should verify the correctness of all updates to the  object/program state, otherwise the strength of the test oracles is considered not enough to guard the program against faults.

Also Known As:

* 

Code Example::

References:
  * On adequacy of assertions in automated test suites: an empirical investigation

Incidental coverage
^^^^^^^^^^^^^^^^^^^

Definitions:

* Is it enough to know that your test suite encounters every line of code? Or don’t you want to be sure that it exercises every line? If you simply encounter the line without asserting that it produces the correct results, are you any better off?

Also Known As:

* 

Code Example::

References:
  * Testing anti-patterns: How to fail with 100% test coverage

Invisible Assertions
^^^^^^^^^^^^^^^^^^^^

Definitions:

* A test which lacks any explicit assertions, leading future readers in the potentially frustrating position of puzzling over the intention of the test.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Missed fail rotten green test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests where the test engineer passes to an assertion primitive to force the test to fail. Such assertion calls are intended to be executed only if something goes wrong, and not if the test passes.

Also Known As:

* 

Code Example::

References:
  * Rotten green tests in Java, Pharo and Python

Missed Fail Rotten Green Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests that do not execute one or many assertions, and do not fall into any of the previous Rotten Green categories

Also Known As:

* 

Code Example::

References:
  * RTj: a Java framework for detecting and refactoring rotten green test cases

Missing Assertions
^^^^^^^^^^^^^^^^^^

Definitions:

* The subject includes behavior which is not asserted by the test, whether implicitly or explicitly.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Missing Assertions
^^^^^^^^^^^^^^^^^^

Definitions:

* the test method consists of an empty block

Also Known As:

* 

Code Example::

References:
  * JUnit Anti-patterns

No Assertions
^^^^^^^^^^^^^

Definitions:

* Tests that have no assertions and require the manual verification of log outputs

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Over exertion assertion
^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where the implementation of an assertion is heavy and in the body of the test, rather than in an assertion library

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Premature Assertions
^^^^^^^^^^^^^^^^^^^^

Definitions:

* Intermingled with a test's set-up of the data and objects it depends on are assertions which attempt to ensure that set-up was successful. The net effect of this often resembles a "Arrange-Assert-Act-Assert" pattern.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Primitive Assertion
^^^^^^^^^^^^^^^^^^^

Definitions:

* Assertions that use primitive content to express intent

Also Known As:

* 

Code Example::

References:
  * Developer test anti-patterns by lasse koskela

Redundant Assertion
^^^^^^^^^^^^^^^^^^^

Definitions:

* extra calls to an assert method where the condition being tested is a hard coded true value.

Also Known As:

* 

Code Example::

References:
  * JUnit Anti-patterns

Redundant Assertion
^^^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when test methods contain assertion statements that are either always true or always false. A test is intended to return a binary outcome of whether the intended result is correct or not, and should not return the same output regardless of the input.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Redundant Assertion
^^^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when test methods contain assertion statements that are either always true or always false. This smell is introduced by developers for debugging purposes and then forgotten.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Redundant Assertion
^^^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when test methods contain assertion statements that are either always true or always false. A test is intended to return a binary outcome of whether the intended result is correct or not, and should not return the same output regardless of the input.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Second guess the calculation 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where rather than using concrete test data, we use something that needs us to calculate the correct answer ahead of assertion

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Self-Test
^^^^^^^^^

Definitions:

* Tests that do not compare a result with an expected value, but with the result itself

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Sensitive Equality
^^^^^^^^^^^^^^^^^^

Definitions:

* A test case with an assertion that compares the state of objects by means of their textual representation, i.e., by means of the result of toString().

Also Known As:

* 

Code Example::

References:
  * Assessing diffusion and perception of test smells in scala projects

Sensitive Equality
^^^^^^^^^^^^^^^^^^

Definitions:

* van Deursen et al. [18] state the agility and ease to write equality checks using the toString() method, being a frequent alternative to calculate a result value and map it to a sequence to compare to a literal string representing the expected value. However, these tests can depend on many irrelevant details, such as commas,  quotes, and spaces. And whenever the toString() method for an object is changed, all related tests will start to fail.

Also Known As:

* 

Code Example::

References:
  * Refactoring Test Smells: A Perspective from Open-Source Developers

Sensitive Equality
^^^^^^^^^^^^^^^^^^

Definitions:

* When an test checks for equality through the use of the toString method.

Also Known As:

* 

Code Example::

References:
  * Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities

Sensitive Equality
^^^^^^^^^^^^^^^^^^

Definitions:

* Occurs when the toString method is used within a test method. Test methods verify objects by invoking the default toString() method of the object and comparing the output against an specific string. Changes to the implementation of toString() might result in failure. The correct approach is to implement a custom method within the object to perform this comparison.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Testing The Internal Monologue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Where the writer of the test has been so focused on the lines of code in their implementation that they haven’t sought ways to observe the behaviour of the system from the outside.

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Under-the-carpet Failing Assertion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A test having the smell Under-the-carpet failing Assertion is a test that returns a successful test-result, but contains hidden assertions. A hidden assertion is an assertion that is put into comments, is not executed when the test runs, and which would actually throw an Error or Failure if the comment were removed.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Under-the-carpet failing Assertion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Failing assertions put into comments

Also Known As:

* 

Code Example::

References:
  * Rule-based Assessment of Test Quality

Using the Wrong Assert
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* There are a large number of different methods beginning with assert defined in the Assert class. Each of these methods has slightly different arguments and semantics about what they are asserting. However, many programmers seem to stick with a single assertion method: assertTrue, and then force the argument of this method into the required boolean expression.

Also Known As:

* 

Code Example::

References:
  * JUnit Anti-patterns

Issues in teardown
------------------

Activation Asymmetry
^^^^^^^^^^^^^^^^^^^^

Definitions:

* A default activation has no matching subsequent deactivation in the same statement block, or a deactivation has no matching previous activation.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Complex Teardown
^^^^^^^^^^^^^^^^

Definitions:

* Complex fixture teardown code is more likely to leave test environment corrupted by not cleaning up correctly. It is hard to verify that it has been written correctly and can easily result in "data leaks" that may later cause this or other tests to fail for no apparent reason.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

External shared-state corruption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Integration tests with shared resources and no rollback

Also Known As:

* 

Code Example::

References:
  * Chapter 8. The pillars of good unit tests

Shared-state corruption 
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests sharing in-memory state without rolling back

Also Known As:

* 

Code Example::

References:
  * Chapter 8. The pillars of good unit tests

Unrepeatable Test
^^^^^^^^^^^^^^^^^

Definitions:

* A test behaves differently the first time it is run than how it behaves on subsequent test runs.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Issues in setup
---------------

Badly Used Fixture
^^^^^^^^^^^^^^^^^^

Definitions:

* A Badly Used Fixture is a xture that is not fully used by the tests in the test-suite.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Bury The Lede
^^^^^^^^^^^^^

Definitions:

* A test's setup is so onerous that the reader forgets the purpose of the subject by the time they reach the relevant invocation and assertion of the subject.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Complicated set up scenarios within the tests themselves
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Whilst there’s a place for automated end-to-end scenarios (I call these user journies), I prefer most acceptance tests to jump straight to the point.

Also Known As:

* 

Code Example::

References:
  * Five automated acceptance test anti-patterns

Curdled Test Fixtures 
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where there’s an inappropriate union of tests in the same fixture, or splitting into multiple fixtures where one would be better

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Excessive setup
^^^^^^^^^^^^^^^

Definitions:

* Many dependencies you have to create beforehand (such as classes, operating system dependencies, databases - basically anything that removes the attention to the testing goal).

Also Known As:

* 

Code Example::

References:
  * TDD anti patterns - Chapter 1

Excessive setup
^^^^^^^^^^^^^^^

Definitions:

* Many dependencies you have to create beforehand (such as classes, operating system dependencies, databases - basically anything that removes the attention to the testing goal).

Also Known As:

* 

Code Example::

References:
  * TDD anti-patterns - the liar, excessive setup, the giant, slow poke

General Fixture
^^^^^^^^^^^^^^^

Definitions:

* A test fixture that is too general. Ideally, test cases should use all the fields provided by their fixture. This might be difficult to uphold when the fixture is shared by several test cases.

Also Known As:

* 

Code Example::

References:
  * Assessing diffusion and perception of test smells in scala projects

General Fixture
^^^^^^^^^^^^^^^

Definitions:

* When the fixture is then reused and augmented by each test to create the necessary setup

Also Known As:

* 

Code Example::

References:
  * Let’s not

General Fixture
^^^^^^^^^^^^^^^

Definitions:

* The test is building or referencing a larger fixture than is needed to verify the functionality in question.

Also Known As:

* 

Code Example::

References:
  * Obscure Test

General Fixture
^^^^^^^^^^^^^^^

Definitions:

* A test fixture that is too general. Ideally, test cases should use all the fields provided by their fixture. This might be difficult to uphold when the fixture is shared by several test cases.

Also Known As:

* 

Code Example::

References:
  * SoCRATES: Scala radar for test smells

General Fixture
^^^^^^^^^^^^^^^

Definitions:

* Occurs when a test case fixture is too general and the test methods only access part of it. A test setup/fixture method that initializes fields that are not accessed by test methods indicates that the fixture is too generalized. A drawback of it being too general is that unnecessary work is being done when a test method is run.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Idle PTC
^^^^^^^^

Definitions:

* A PTC is created but never started. A PTC which is not started is of no use for the test case.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Irrelevant Information
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* The test is exposing a lot of irrelevant details about the fixture that distract the test reader from what really affects the behavior of the SUT.

Also Known As:

* 

Code Example::

References:
  * Obscure Test

Isolated PTC
^^^^^^^^^^^^

Definitions:

* A PTC is created and started, but neither connected to another component nor mapped to the TSI. A PTC which is not connected or mapped is isolated from all other components, especially the MTC, and is of no use for the test.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Noisy setup
^^^^^^^^^^^

Definitions:

* When a verbose sequence of low-level records that is difficult to comprehend is displayed in the setup

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns: Fixtures and Factories

Oversharing on setup
^^^^^^^^^^^^^^^^^^^^

Definitions:

* where every test sets up a lot of shared data which only some tests need

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Superfluous Setup Data
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Occurs when testing queries or filters, in which you only expect to get a subset of the data back. The underlying idea is that, in order to be thorough, “extra” data should be present to show that the query or filter works as required.

Also Known As:

* 

Code Example::

References:
  * Testing anti-patterns

Test setup is somewhere else
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where the test method just does the assertions, not the given/when part
*  this can be acceptable in the case of several tests on a single shared expensive resource setup, but seldom is at other times

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Unused Definition
^^^^^^^^^^^^^^^^^

Definitions:

* Unused code should be removed. Note that only local definitions can be removed safely because they cannot be accessed from outside the defining unit. For global definitions there might exist references in modules which have not been considered.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Using fixtures
^^^^^^^^^^^^^^

Definitions:

* When a test uses fixtures to prepare and reuse test data on Rails

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns: Fixtures and Factories

Issues in exception handling
----------------------------

Catching Unexpected Exceptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When writing production code, developers are generally aware of the problems of uncaught exceptions, and so are relatively diligent about catching exceptions and logging the problem. In the case of unit tests, however, this pattern is completly wrong!

Also Known As:

* 

Code Example::

References:
  * JUnit Anti-patterns

Exception Handling
^^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when the passing or failing of a test method is explicitly dependent on the production method throwing an exception. Developers should utilize JUnit’s exception handling features to automatically pass/fail the test instead of custom exception handling code or exception throwing.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Exception Handling
^^^^^^^^^^^^^^^^^^

Definitions:

* Occurs when the test manually handles both exceptions and test outcome

Also Known As:

* 

Code Example::

References:
  * Refactoring Test Smells: A Perspective from Open-Source Developers

Exception Handling
^^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when a test method explicitly a passing or failing of a test method is dependent on the production method throwing an exception. Developers should utilize JUnit's exception handling to automatically pass/fail the test instead of writing custom exception handling code or throwing an exception.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Exception Handling
^^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when the passing or failing of a test method is explicitly dependent on the production method throwing an exception. Developers should utilize JUnit’s exception handling features to automatically pass/fail the test instead of custom exception handling code or exception throwing.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Expected Exceptions and Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A verification happens after an expected exception is thrown and halts the test method execution

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Expecting Exceptions Anywhere
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests that do not track the step that raised the expected exception and pass

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

The Secret Catcher
^^^^^^^^^^^^^^^^^^

Definitions:

* A test that at first glance appears to be doing no testing, due to absence of assertions. But "The devil is in the details".. the test is really relying on an exception to be thrown and expecting the testing framework to capture the exception and report it to the user as a failure.

Also Known As:

* 

Code Example::

References:
  * Unit testing Anti-patterns catalogue

The Silent Catcher
^^^^^^^^^^^^^^^^^^

Definitions:

* A test that passes if an exception is thrown.. even if the exception that actually occurs is one that is different than the one the developer intended.

Also Known As:

* 

Code Example::

References:
  * Unit testing Anti-patterns catalogue

Code related
============

Violating coding best practices
-------------------------------

Anonymous Test
^^^^^^^^^^^^^^

Definitions:

* An anonymous test is a test whose name is meaningless as it doesn't express the purpose of the test in the current context. However tests can be regarded as documentation, and the name is an important part of that as it should abstract what the test is all about.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Bad Documentation Comment
^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A documentation comment does not conform to its format. Documentation comments like T3Doc need to conform to certain formatting rules and appear at certain positions in the source code.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Bad Naming
^^^^^^^^^^

Definitions:

* An identifier does not conform to a given naming convention. Before this smell can be detected, the naming conventions have to be agreed on. Proposed naming conventions for TTCN-3 can be found on the official TTCN-3 home page.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Bad Naming
^^^^^^^^^^

Definitions:

* When a test fails, or when the test base requires maintenance, the test names are the first thing developers will generally attempt to understand before they apply changes to the test or the code being tested. If test names are poor quality, developers will need to spend time reading the code and determining how the test’s actual behavior is related to its name

Also Known As:

* 

Code Example::

References:
  * Test Naming Failures. An Exploratory Study of Bad Naming Practices in Test Code

Blethery prefixes
^^^^^^^^^^^^^^^^^

Definitions:

* where the implementation of a single line of test code is prefixed by a lot of characters before we get to the point

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Constant Actual Parameter Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* The value of an actual parameter is the same for all occurances. In contrast to Unused Parameter (4.3.1), the parameter is in use within the declaring entity and must not simply be removed. The declaring entity could be a template or a behavioral entity (function, test case or altstep).

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Default Test
^^^^^^^^^^^^

Definitions:

* By default Android Studio creates default test classes when a project is created. These template test classes are meant to serve as an example for developers when writing unit tests and should either be removed or renamed. Having such files in the project will cause developers to start adding test methods into these files, making the default test class a container of all test cases and violate good testing practices. Problems would also arise when the classes need to be renamed in the future.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Default Test
^^^^^^^^^^^^

Definitions:

* By default Android Studio creates default test classes when a project is created. These classes are meant to serve as an example for developers when wring unit tests and should either be removed or renamed. Having such files in the project will cause developers to start adding test methods into these files, making the default test class a container of all test cases. This also would possibly cause problems when the classes need to be renamed in the future.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Default Test
^^^^^^^^^^^^

Definitions:

* By default Android Studio creates default test classes when a project is created. These template test classes are meant to serve as an example for developers when writing unit tests and should either be removed or renamed. Having such files in the project will cause developers to start adding test methods into these files, making the default test class a container of all test cases and violate good testing practices. Problems would also arise when the classes need to be renamed in the future.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Directly executing JavaScript
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Since WebDriver can directly execute any arbitrary JavaScript, it can be tempting to bypass DOM manipulation and just run the JavaScript.

Also Known As:

* 

Code Example::

References:
  * Five automated acceptance test anti-patterns

Empty Test
^^^^^^^^^^

Definitions:

* Occurs when a test method has no executable statements. Such methods are possibly created for debugging purposes without being deleted or contain commented-out test statements. An empty test method can be considered problematic and more dangerous than not having a test case at all since JUnit will indicate that the test passes even if there are no executable statements present in the method body. As such, developers introducing behavior-breaking changes into production class, will not be notified of the alternated outcomes as JUnit will report the test as passing.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Empty Test
^^^^^^^^^^

Definitions:

* Occurs when a test method does not contain executable statements. Such methods are possibly created for debugging purposes and then forgotten about or contains commented out code. An empty test can be considered problematic and more dangerous than not having a test case at all since JUnit will indicate that the test passes even if there are no executable statements present in the method body. As such, developers introducing behavior-breaking changes into production class, will not be notified of the alternated outcomes as JUnit will report the test as passing.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Empty Test
^^^^^^^^^^

Definitions:

* Occurs when a test method has no executable statements. Such methods are possibly created for debugging purposes without being deleted or contain commented-out test statements. An empty test method can be considered problematic and more dangerous than not having a test case at all since JUnit will indicate that the test passes even if there are no executable statements present in the method body. As such, developers introducing behavior-breaking changes into production class, will not be notified of the alternated outcomes as JUnit will report the test as passing.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Erratic Tests
^^^^^^^^^^^^^

Definitions:

* tests that will pass or fail without you changing anything

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns

Everything is a property
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where a test class keeps what should be temporary variables in instance variables

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Flaky locator
^^^^^^^^^^^^^

Definitions:

* A key component to making UI automation work is to provide your tool with identifiers to the elements that you'd like it to find and interact with. Using flaky locators—ones that are not durable—is an awful code smell. 

Also Known As:

* 

Code Example::

References:
  * Writing good gherkin

Fully-Parameterized Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* All fields of a template are defined by formal parameters.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Goto Statement
^^^^^^^^^^^^^^

Definitions:

* A goto statement is used. The use of goto statements is inadvisable and should be avoided.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Hidden Meaning 
^^^^^^^^^^^^^^^

Definitions:

* where something that should be part of the execution of the test, and appear in a test report, is hidden in a comment – essentially comment instead of name

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Hidden test call 
^^^^^^^^^^^^^^^^^

Definitions:

* Tests calling other tests

Also Known As:

* 

Code Example::

References:
  * Chapter 8. The pillars of good unit tests

Ignored Test
^^^^^^^^^^^^

Definitions:

* JUnit 4 provides developers with the ability to suppress test methods from running. However, these ignored test methods result in overhead with regards to compilation time and an increase in code complexity and comprehension

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Ignored Test
^^^^^^^^^^^^

Definitions:

* JUnit 4 provides developers with the ability to suppress test methods from running. However, these ignored test methods result in overhead since they add unnecessary overhead with regards to compilation time, and increases code complexity and comprehension.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Ignored Test
^^^^^^^^^^^^

Definitions:

* JUnit 4 provides developers with the ability to suppress test methods from running. However, these ignored test methods result in overhead with regards to compilation time and an increase in code complexity and comprehension

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Is There Anybody There? 
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* any flickering test that occasionally breaks a build – bad test or bad code?

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Literal Pollution
^^^^^^^^^^^^^^^^^

Definitions:

* When writing tests for the application code it is mostly required also to provide some data to be able to test the functionality. This is mostly done by dening literals in the test code. However an excessive use of literals can cause severe problems:
- Too many literals are distracting and obfuscate the functionality and purpose of a test. This makes a test hard to read and understand. 
- The same or similar test data is often repeated within a test or testsuite. This is often a consequence of simply extending or adding tests without actually designing them. The result is a test-suite that is extremely hard to maintain and refactor. We detected such Duplication in harvesting our case study.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Long Parameter List
^^^^^^^^^^^^^^^^^^^

Definitions:

* High number of formal parameters.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Missed skip rotten green test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test methods contain guards to stop their execution early under certain conditions.

Also Known As:

* 

Code Example::

References:
  * Rotten green tests in Java, Pharo and Python

Missing Variable Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A variable or out parameter is read before its value has been defined. Access to undefined variables might result in unpredictable behavior.

Also Known As:

* UR data flow anomaly

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Missing Verdict
^^^^^^^^^^^^^^^

Definitions:

* A test case does not set a verdict. Normally a test case should set a verdict before terminating.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Name-clashing Import
^^^^^^^^^^^^^^^^^^^^

Definitions:

* An imported element causes a name clash with a declaration in the importing module or another imported element.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Nondeterministic Test
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test failures occur at random even when only a single Test Runner is running tests.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Over-specific Runs On
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A behavioral entity (function, test case or altstep) is declared to run on a component, but uses only elements of this component’s super-component or no elements of the component at all.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Overreferencing
^^^^^^^^^^^^^^^

Definitions:

* It is about test-methods referencing many times classes from the application code. The main problem with an Overreferencing Test is that it causes a lot of unnecessary dependencies towards the model code. That distracts from the goal of the test.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Overreferencing
^^^^^^^^^^^^^^^

Definitions:

* Test creating unnecessary dependencies and causing duplication

Also Known As:

* 

Code Example::

References:
  * Rule-based Assessment of Test Quality

Short Template
^^^^^^^^^^^^^^

Definitions:

* template definition is very short (in terms of characters or number of fields).

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Singular Component Variable/Constant/Timer Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A component variable, constant or timer is referenced by one single function, test case or altstep only, although other behavioral entities run on the component as well.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Singular Template Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A template definition is referenced only once.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Stop in Function
^^^^^^^^^^^^^^^^

Definitions:

* A function contains a stop statement. If possible, functions should not contain any stop statement, because this can prevent the execution of postambles (e.g. code that has to be executed after each test case). Instead, functions should use return values. However, this smell should be classified weak compared to other smells.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Test body is somewhere else
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* when the test method calls another method entirely with no other implementation in the test method – often a sign of missing parameterised test

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

The Stepford Fields
^^^^^^^^^^^^^^^^^^^

Definitions:

* where (too) many of the fields in test contain the same value, making it hard to spot when a calculation is reading a value from the wrong field, because it works on the test data
*  this also makes load testing near a cache pretty meaningless

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Time Bombs
^^^^^^^^^^

Definitions:

* Tests that fail due to ever-so-slightly different time values, during certain days of the week or month, or when a long-running time-sensitive test straddles two hours, days, weeks, months, or years and the code can't handle it.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Time Sensitive Test
^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests that only pass depending on the time of the day they are executed

Also Known As:

* 

Code Example::

References:
  * A testing anti-pattern safari

Unreachable Default
^^^^^^^^^^^^^^^^^^^

Definitions:

* An alt statement contains an else branch while a default is active. The else branch of an alt statement is taken if no other branch is applicable. If a default is active at the same time, its branches come after all branches of the alt statement. Hence the default altstep can never be executed if an else branch is present.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Unrestricted Imports
^^^^^^^^^^^^^^^^^^^^

Definitions:

* A module imports more from another module than needed.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Unused Imports
^^^^^^^^^^^^^^

Definitions:

* An import from another module is never used.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Unused Parameter
^^^^^^^^^^^^^^^^

Definitions:

* A parameter is never used within the declaring unit. For in-parameters, the parameter is never read, for out-parameters never defined, for inout-parameters never accessed at all.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Unused Variable Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A defined variable or in parameter is not read before it becomes undefined.

Also Known As:

* DU data flow anomaly

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Wasted Variable Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A variable is defined and defined again before it is read.

Also Known As:

* DD data flow anomaly

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Complex / Hard to understand
----------------------------

Bad Comment Rate
^^^^^^^^^^^^^^^^

Definitions:

* The comment rate (number of comments per line) is too high or too low.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Hard-Coded Test Data
^^^^^^^^^^^^^^^^^^^^

Definitions:

* Data values in the fixture, assertions or arguments of the SUT are hard-coded in the Test Method obscuring cause-effect relationships between inputs and expected outputs.

Also Known As:

* 

Code Example::

References:
  * Obscure Test

Hard-Coded Values
^^^^^^^^^^^^^^^^^

Definitions:

* Scalar values or value objects that are used directly in fixture setup, as parameters in the test exercise or as expected values in the verification. That is, they are not assigned to a named constant or variable.

Also Known As:

* 

Code Example::

References:
  * Test Smell: Hard Coded Values

Herp Derp
^^^^^^^^^

Definitions:

* words and comments in test code or names that add nothing, like simple or test or //given

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

It looks right to me 
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where the test data for negative cases makes the test hard to understand

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Long Statement Block
^^^^^^^^^^^^^^^^^^^^

Definitions:

* Long statement block in function, test case or altstep. A long function is more difficult to understand than a short one. Although the use of short functions (i.e. methods) is especially important for modern objectoriented languages, short functions have a certain importance for TTCN-3 as well. Long statement blocks in functions, test cases and altsteps should be decomposed into short functions with meaningful names.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Long Test
^^^^^^^^^

Definitions:

* A test method is so long that it's testing multiple things.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Long Test
^^^^^^^^^

Definitions:

* A Long Test is a test that consists of lot of code and statements. Such tests are mostly (but not necessarily) complex and badly document the purpose of the test and the application code. Furthermore they tend to test too much functionality, maybe even getting eager.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Magic Number
^^^^^^^^^^^^

Definitions:

* When the significance of the numeric literals that was passed as parameter in the assertion method is unknowed

Also Known As:

* 

Code Example::

References:
  * Test Artifacts — The Practical Testing Book

Magic Number Test
^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when a test method contains unexplained and undocumented numeric literals as parameters or as values to identifiers. These magic values do not sufficiently indicate the meaning/purpose of the number. Hence, they hinder code understandability. Consequently, they should be replaced with constants or  variables, thereby providing a descriptive name for the value.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Magic Number Test
^^^^^^^^^^^^^^^^^

Definitions:

* Occurs when the test method contains undocumented numeric literals with no clear meaning (magic values).

Also Known As:

* 

Code Example::

References:
  * Refactoring Test Smells: A Perspective from Open-Source Developers

Magic Number Test
^^^^^^^^^^^^^^^^^

Definitions:

* Occurs when assert statements in a test method contain numeric literals (i.e., magic numbers) as parameters. Magic numbers do not indicate the meaning/purpose of the number. Hence, they should be replaced with constants or variables, thereby providing a descriptive name for the input.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Magic Number Test
^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when a test method contains unexplained and undocumented numeric literals as parameters or as values to identifiers. These magic values do not sufficiently indicate the meaning/purpose of the number. Hence, they hinder code understandability. Consequently, they should be replaced with constants or  variables, thereby providing a descriptive name for the value.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Magic Values
^^^^^^^^^^^^

Definitions:

* Magic Values are literals not defined as constant. Numeric literals are called Magic Numbers, string literals are called Magic Strings.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Obscure Test
^^^^^^^^^^^^

Definitions:

* It is difficult to understand the test at a glance. Automated tests should serve at least two purposes. First, they should act as documentation of how the system under test (SUT) should behave
*  we call this Tests as Documentation (see Goals of Test Automation on page X). Second, they should be a self-verifying executable specification. These two goals are often contradictory because the level of detailed needed for tests to be executable may make the test so verbose as to be difficult to understand.

Also Known As:

* Long Test, Complex Test, Verbose Test

Code Example::

References:
  * Obscure Test

Obscure Test
^^^^^^^^^^^^

Definitions:

* A test that has a lot of noise in it, noise that’s making it hard to discern what the test is actually doing.

Also Known As:

* 

Code Example::

References:
  * Test smell: Obscure Test

Obscure Tests
^^^^^^^^^^^^^

Definitions:

* Where it is hard to figure out exactly what is being tested

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns

Over refactoring of tests
^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where you can’t read them because they’ve been DRYed out to death

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Overcommented Test
^^^^^^^^^^^^^^^^^^

Definitions:

* Overcommented Tests dene too many comments, obfuscating the code and distracting from the purpose of the test.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Self Important Test Data
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test data is more complex than is needed to exercise some behavior in a test.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Using complicated x-path or CSS selectors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Using element identification selectors that have long chains from the DOM in them leads to fragile tests, as any change to that chain in the DOM will break your tests.

Also Known As:

* 

Code Example::

References:
  * Five automated acceptance test anti-patterns

In association with production code
-----------------------------------

code pollution
^^^^^^^^^^^^^^

Definitions:

* It takes place when you introduce additional code to your main code base in order to enable unit testing

Also Known As:

* 

Code Example::

References:
  * Code pollution

Context Logic in Production Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When the production code becomes aware of the context in which it is used.

Also Known As:

* 

Code Example::

References:
  * Unit Testing Smells: What Are Your Tests Telling You?

Equality Pollution
^^^^^^^^^^^^^^^^^^

Definitions:

* The code that is put into production contains logic that should be exercised only during tests… A system that behaves one way in the test lab and an entirely different way in production is a recipe for disaster!

Also Known As:

* 

Code Example::

References:
  * How to Compare Object Instances in your Unit Tests Quickly and Easily

Fire And Forget
^^^^^^^^^^^^^^^

Definitions:

* A test that's at risk of exiting prematurely, typically before its assertions can run and fail the test run if necessary

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Overspecification
^^^^^^^^^^^^^^^^^

Definitions:

* Tests increasingly serve multiple roles in today’s projects. They help us design APIs through test-driven development. They provide confidence that new changes aren’t breaking existing functionality. They offer an executable specification of the application. But can we ever get to a point where we have too much testing?

Also Known As:

* 

Code Example::

References:
  * Testing anti-patterns: How to fail with 100% test coverage

Overspecified Tests
^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests that specify too many things that aren’t genuinely related to the scenario being tested.

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Plate Spinning
^^^^^^^^^^^^^^

Definitions:

* 

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Production Logic in Test
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Some forms of Conditional Test Logic are found in the result verification section of our tests.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Test Hook
^^^^^^^^^

Definitions:

* Conditional logic within the SUT determines whether the "real" code or test-specific logic is run.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Test Hooks
^^^^^^^^^^

Definitions:

* having specific methods or branches in your production code for testing.

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns

Test tautology
^^^^^^^^^^^^^^

Definitions:

* Generally speaking one does not want to duplicate the logic between tests and code. So replicating a regexp or something else in the test is not an option.

Also Known As:

* 

Code Example::

References:
  * How to write good tests

The ugly mirror
^^^^^^^^^^^^^^^

Definitions:

* When you occasionally find yourself staring at a spec that looks exactly like the code under test, there’s surprisingly little win left to enjoy.

Also Known As:

* 

Code Example::

References:
  * Testing anti-patterns: How to fail with 100% test coverage

The ugly mirror
^^^^^^^^^^^^^^^

Definitions:

* When you occasionally find yourself staring at a spec that looks exactly like the code under test

Also Known As:

* 

Code Example::

References:
  * Testing anti-patterns: The ugly mirror

Code duplication
----------------

Duplicate Alt Branches
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Different alt constructs contain duplicate branches

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Duplicate Assert
^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when a test method tests for the same condition multiple times within the same test method. If the test method needs to test the same condition using different values, a new test method should be created. As a best practice, the name of the test method should be an indication of the test being performed. Possible situations that would give rise to this smell include (1) developers grouping multiple conditions to test a single method, (2) developers performing debugging activities, and (3) an accidental copy-paste of code

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Duplicate Assert
^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when a test method tests for the same condition multiple times within the same test method. If the test method needs to test the same condition using different values, a new test method should be utilized
*  the name of the test method should be an indication of the test being performed. Possible situations that would give rise to this smell include: (1) developers grouping multiple conditions to test a single method
*  (2) developers performing debugging activities
*  and (3) an accidental copy-paste of code.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Duplicate Assert
^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when a test method tests for the same condition multiple times within the same test method. If the test method needs to test the same condition using different values, a new test method should be created. As a best practice, the name of the test method should be an indication of the test being performed. Possible situations that would give rise to this smell include (1) developers grouping multiple conditions to test a single method, (2) developers performing debugging activities, and (3) an accidental copy-paste of code

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Duplicate Component Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Two or more components declare identical variables, constants, timers or ports.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Duplicate In-Line Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Two or more similar or identical in-line templates.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Duplicate Local Variable/Constant/Timer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* The same local variable, constant or timer is defined in two or more functions, test cases or altsteps running on the same component.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Duplicate Statements
^^^^^^^^^^^^^^^^^^^^

Definitions:

* A duplicate sequence of statements in the statement block of one or multiple behavioral entities (functions, test cases and altsteps).

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Duplicate Template Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* The fields of two or more templates are identical or very similar

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Duplicated code
^^^^^^^^^^^^^^^

Definitions:

* If you have duplicated code in tests, it makes it harder to refactor the implementation code because you have a disproportionate number of tests to update. Tests should help you refactor with confidence, rather than be a large burden that impedes your work on the code being tested.

Also Known As:

* 

Code Example::

References:
  * Is duplicated code more tolerable in unit tests?

Duplicated Code in Conditional
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* The duplicated code can appear in a series of conditionals (with different conditions and the same action in each check) or in all legs of a conditional

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Half a helper method 
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where there’s a utility method to help a test do its job, yet all calls to it are immediately followed by the exact same code. This is because the method is only doing half the job it should, so your test has more boilerplate in it.

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Missing parameterised test
^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* when you did it the long way round because you didn’t bring in parameterisation

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Missing test data factory
^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where every test has its own way of making the same test example data

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Test Code Duplication
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Repeated test code steps

Also Known As:

* 

Code Example::

References:
  * LCCSS: A Similarity Metric for Identifying Similar Test Code

Test Code Duplication
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* This test smell normally identifies classes that contain test methods with repeated test code steps.

Also Known As:

* 

Code Example::

References:
  * Refactoring Test Smells: A Perspective from Open-Source Developers

Test Code Duplication
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When several tests in a suite needs to be setup or do similar computations

Also Known As:

* 

Code Example::

References:
  * Test Artifacts — The Practical Testing Book

Test Code Duplication
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* The same test code is repeated many times.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

The First and Last Rites 
^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where there’s some ritual/boilerplate at the start and end of most test bodies, suggesting a lack of common setup/teardown code

Also Known As:

* Oops I Forgot the Setup

Code Example::

References:
  * Test Smells - The Coding Craftsman

Two for the price of one
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* sometimes a sign of missing parameterised tests – where a single test case is testing two use cases with the same set up

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Mock and stub related
---------------------

Is Mockito Working Fine?
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When the mock framerwork is tested intead of the SUT

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Mock’em All!
^^^^^^^^^^^^

Definitions:

* When a test overuse all kinds of test double, even when it is not really the best option

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Mockers Without Borders
^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests demonstrate little rhyme or reason for whether a given test ought to fake a particular dependency or call through to the real thing.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Mockito any() vs. isA()
^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Misuse of mockito’s matchers classes to type checks

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Remote Control Mocking
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* where a class that depends on a service is tested with those service’s complex dependencies mocked, rather than the service itself being mocked.

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Surreal
^^^^^^^

Definitions:

* A test whose use of test doubles is so confusing, it's hard to tell what the test is even doing at run-time.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

The Dead Tree
^^^^^^^^^^^^^

Definitions:

* A test which where a stub was created, but the test wasn't actually written.

Also Known As:

* Process Compliance Backdoor

Code Example::

References:
  * Unit testing Anti-patterns catalogue

Test semantic/logic
===================

Testing many things
-------------------

Assertion Roulette
^^^^^^^^^^^^^^^^^^

Definitions:

* A test case that contains more than one assertion of which at least one does not provide a reason for assertion failure. In case the test fails, this test smell encumbers identifying which assertion failed and the reason why

Also Known As:

* 

Code Example::

References:
  * Assessing diffusion and perception of test smells in scala projects

Assertion Roulette
^^^^^^^^^^^^^^^^^^

Definitions:

* In test cases affected by this smell, it is hard to tell which of several assertions failed.

Also Known As:

* 

Code Example::

References:
  * Did You Remember To Test Your Tokens?

Assertion Roulette
^^^^^^^^^^^^^^^^^^

Definitions:

* collection of unexplained assertions in a single test method that makes it difficult to trace which exact assertion had a problem in the event of test failure

Also Known As:

* 

Code Example::

References:
  * Refactoring Test Smells: A Perspective from Open-Source Developers

Assertion Roulette
^^^^^^^^^^^^^^^^^^

Definitions:

* A test that has multiple assertion statements that do not provide any description of why they failed

Also Known As:

* 

Code Example::

References:
  * Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities

Assertion Roulette
^^^^^^^^^^^^^^^^^^

Definitions:

* Occurs when a test method has multiple non-documented assertions. Multiple assertion statements in a test method without a descriptive message impacts readability/understandability/maintainability as it’s not possible to understand the reason for the failure of the test.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Assertion Roulette
^^^^^^^^^^^^^^^^^^

Definitions:

* When a test method has many unexplained assertions, making it hard to tell which one may cause a test failure

Also Known As:

* 

Code Example::

References:
  * Test Artifacts — The Practical Testing Book

Eager Test
^^^^^^^^^^

Definitions:

* A test case that checks or uses more than one method of the class under test. Since its introduction [3], this smell has been somewhat broadly defined. It is left to interpretation which method calls count towards the maximum. Either all methods invoked on the class under test could count, or only the methods invoked on the same instance under test, or only the methods of which the return value is eventually used within an assertion.

Also Known As:

* 

Code Example::

References:
  * Assessing diffusion and perception of test smells in scala projects

Eager Test
^^^^^^^^^^

Definitions:

* The test is verifying too much functionality in a single Test Method.

Also Known As:

* 

Code Example::

References:
  * Obscure Test

Eager Test
^^^^^^^^^^

Definitions:

* A test that checks multiple different functionalities in one case, which makes it hard to read or understand.

Also Known As:

* 

Code Example::

References:
  * Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities

Eager Test
^^^^^^^^^^

Definitions:

* A test method that at- tempts to test several behaviors of the tested object.

Also Known As:

* The Test It All, Split Personality

Code Example::

References:
  * Smells in software test code: A survey of knowledge in industry and academia

Eager Test
^^^^^^^^^^

Definitions:

* Occurs when a test method invokes several methods of the production object. This smell results in difficulties in test comprehension and maintenance.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Eager Test
^^^^^^^^^^

Definitions:

* A single test verifies too much functionality.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Missing Assertion Message
^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A test fails. Upon examining the output of the Test Runner, we cannot determine exactly which assertion had failed.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Multiple Assertions
^^^^^^^^^^^^^^^^^^^

Definitions:

* When a test method contains multiple assertion statements, it is an indication that the method is testing too much

Also Known As:

* 

Code Example::

References:
  * JUnit Anti-patterns

Split Logic
^^^^^^^^^^^

Definitions:

* When the test logic is split into several test objects and their specific assertions

Also Known As:

* 

Code Example::

References:
  * Developer test anti-patterns by lasse koskela

Split Personality
^^^^^^^^^^^^^^^^^

Definitions:

* A test method that attempts to test several behaviors of the tested object.

Also Known As:

* 

Code Example::

References:
  * Developer test anti-patterns by lasse koskela

The Free Ride
^^^^^^^^^^^^^

Definitions:

* When an extra assertion is added in an existing test to cover a new scenario case

Also Known As:

* Piggyback

Code Example::

References:
  * TDD Anti-patterns: The Free Ride / Piggyback

The Free Ride
^^^^^^^^^^^^^

Definitions:

* rather than write a new test case method to test another/distinct feature/functionality, a new assertion rides along in an existing test case.

Also Known As:

* Piggyback

Code Example::

References:
  * Tdd antipatterns: The free ride

The giant
^^^^^^^^^

Definitions:

* Many assertions in a single test case

Also Known As:

* 

Code Example::

References:
  * TDD anti patterns - Chapter 1

The giant
^^^^^^^^^

Definitions:

* Many assertions in a single test case

Also Known As:

* 

Code Example::

References:
  * TDD anti-patterns - the liar, excessive setup, the giant, slow poke

Other test logic related
------------------------

Branch To Assumption Anti-Pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* An assumption is conditionally executed.

Also Known As:

* 

Code Example::

References:
  * Parameterized Test Patterns For Effective Testing with Pex

Chafing
^^^^^^^

Definitions:

* A test in which the author attempts to eliminate as much textual duplication as possible, even if the indirection it introduces confuses future readers of the intention and behavior of the test.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Complex Conditional
^^^^^^^^^^^^^^^^^^^

Definitions:

* A conditional expression is composed of many boolean conjunctions.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Conditional assertions
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* it makes your test non-deterministic: you will never be sure which path will be verified in the next pass

Also Known As:

* 

Code Example::

References:
  * Anti-patterns in test automation

Conditional Test Logic
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test methods need to be simple and execute all statements in the production method. Conditions within the test method will alter the behavior of the test and its expected output, and would lead to situations where the test fails to detect defects in the production method since test statements were not executed as a condition was not met. Furthermore, conditional code within a test method negatively impacts the ease of comprehension by developers.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Conditional Test Logic
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Cccurs when the test outcome depends on a condition inside the test method

Also Known As:

* 

Code Example::

References:
  * Refactoring Test Smells: A Perspective from Open-Source Developers

Conditional Test Logic
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test methods need to be simple and execute all statements in the production method. Conditions within the test method will alter the behavior of the test and its expected output, and would lead to situations where the test fails to detect defects in the production method since test statements were not executed as a condition was not met. Furthermore, conditional code within a test method negatively impacts the ease of comprehension by developers.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Conditional Test Logic
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test methods need to be simple and execute all statements in the production method. Conditions within the test method will alter the behavior of the test and its expected output, and would lead to situations where the test fails to detect defects in the production method since test statements were not executed as a condition was not met. Furthermore, conditional code within a test method negatively impacts the ease of comprehension by developers.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Conditional Test Logic
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A test contains code that may or may not be executed

Also Known As:

* Indented Test Code

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Conditional Verification Logic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* This is usually caused by wanting to prevent the execution of assertions if the SUT fails to return the right objects or the use of loops to verify the contents of collections returned by the SUT.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Contaminated Test Subject
^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A test somehow morphs its subject into something less realistic for its own purposes and without regard for the resulting erosion in our confidence that the test ensures the subject's behavior under real-world conditions.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Context-Dependent Rotten Green Assertion Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests contain multiple conditional branches with different assertions in each branch

Also Known As:

* 

Code Example::

References:
  * Rotten green tests in Java, Pharo and Python

Context-Dependent Rotten Green Assertion Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Contains conditionals with different assertions in the different branches

Also Known As:

* 

Code Example::

References:
  * RTj: a Java framework for detecting and refactoring rotten green test cases

Embedding implementation detail in your features/scenarios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Acceptance test scenarios are meant to convey intention over implementation. If you start seeing things like URLs in your test scenarios you’re focusing on implementation.

Also Known As:

* 

Code Example::

References:
  * Five automated acceptance test anti-patterns

Evolve or …
^^^^^^^^^^^

Definitions:

* Tests that are not maintained after SUT code evolution and still pass

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Factories with random data instead of sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When used alongside factories, random data generators may compromise the reliability of a test suite.

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns: Fixtures and Factories

Flexible Test
^^^^^^^^^^^^^

Definitions:

* Test code verifies different functionality depending on when or where it is run.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Fully Rotten Green Test
^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Contains an assertion which was forced to fail.

Also Known As:

* 

Code Example::

References:
  * RTj: a Java framework for detecting and refactoring rotten green test cases

Generative
^^^^^^^^^^

Definitions:

* A test loops over a data structure of discrete inputs and expected outputs to generate test cases.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Ground zero
^^^^^^^^^^^

Definitions:

* where the lack of testing with 0 is the source of a lot of bugs.

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Guarded Test
^^^^^^^^^^^^

Definitions:

* Guarded Tests include boolean branching logics like ifTrue: or ifFalse:

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Guarded Test
^^^^^^^^^^^^

Definitions:

* Conditional test including branches like ifTrue:aBlock or ifFalse:aBlock

Also Known As:

* 

Code Example::

References:
  * Rule-based Assessment of Test Quality

Happy Path
^^^^^^^^^^

Definitions:

* A test that uses known input, which executes without exception and produces an expected output.

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Indecisive
^^^^^^^^^^

Definitions:

* A test contains branching logic. Of course, test-scoped logic is always risky, since it is itself untested. But this smell portends some deeper issues worth discussing.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Insufficient Grouping
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A module or group contains too many elements. Especially for large modules, groups should be used to add logical structure to the module and enhance readability. If a group reaches a critical size, it can be structured further by subgroups.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Invasion Of Privacy
^^^^^^^^^^^^^^^^^^^

Definitions:

* A test is written directly against a method that's intended to be a private implementation detail of the subject.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Lazy Test
^^^^^^^^^

Definitions:

* More than one test case with the same fixture that tests the same method. This smell affects test maintainability, as assertions testing the same method should be in the same test case. Like EAGER TEST, the original definition [3] leaves some details to interpretation. We consider every call to the class under test as a potential cause of LAZY TEST, irrespective of whether their results are used in an assertion.

Also Known As:

* 

Code Example::

References:
  * Assessing diffusion and perception of test smells in scala projects

Lazy Test
^^^^^^^^^

Definitions:

* Occurs when multiple test methods invoke the same method of the production object.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Multiple Test Conditions
^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A test is trying to apply the same test logic to many sets of input values each with their own corresponding expected result.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Nested Conditional
^^^^^^^^^^^^^^^^^^

Definitions:

* Nested conditional expression. Use if and else leg of a conditional only if both paths are part of the normal behavior
*  if one leg is an unusual condition, use a separate exit point (guard clause) instead.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Paranoid
^^^^^^^^

Definitions:

* A test (and as a result, its subject) covers edge cases that aren't actually reachable by the production application.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Parsed Data
^^^^^^^^^^^

Definitions:

* A test creates structured data by parsing unstructured input and only uses the structured data during the test.

Also Known As:

* 

Code Example::

References:
  * Parameterized Test Patterns For Effective Testing with Pex

Quixotic
^^^^^^^^

Definitions:

* A test that charts an idealistic path through the subject code, cherry-picking inputs that provide minimum resistance (e.g. in test data setup), which may result in missed test coverage in code that handle negative cases. Notably, this is more likely to occur when those negative cases are also somehow complex, which is precisely when good testing is important!

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Rotten Green Test
^^^^^^^^^^^^^^^^^

Definitions:

* A test that passes (is green) but contains assertions that are never executed

Also Known As:

* 

Code Example::

References:
  * RTj: a Java framework for detecting and refactoring rotten green test cases

Skip Rotten Green Test
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Contains guards to stop their execution early under certain conditions.

Also Known As:

* 

Code Example::

References:
  * RTj: a Java framework for detecting and refactoring rotten green test cases

Tangential
^^^^^^^^^^

Definitions:

* The subject and its test claim to be focused on something, but the bulk of their complexity is focused on a different (often subordinate) responsibility.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Test By Number
^^^^^^^^^^^^^^

Definitions:

* Production code is tested consistently by rote, inadvertently suppressing creativity in the design of both the tests and their subjects.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

The liar
^^^^^^^^

Definitions:

* Testing asynchronous code becomes tricky as it is based on a future value that you might receive or might not.

Also Known As:

* 

Code Example::

References:
  * TDD anti patterns - Chapter 1

The liar
^^^^^^^^

Definitions:

* Testing asynchronous code becomes tricky as it is based on a future value that you might receive or might not.

Also Known As:

* 

Code Example::

References:
  * TDD anti-patterns - the liar, excessive setup, the giant, slow poke

Underspecification
^^^^^^^^^^^^^^^^^^

Definitions:

* While it’s clearly possible for a test suite to do too much, it’s far more common for it to do too little.

Also Known As:

* 

Code Example::

References:
  * Testing anti-patterns: How to fail with 100% test coverage

Use Smart Values
^^^^^^^^^^^^^^^^

Definitions:

* Tests pass when the scenario they test is not really fulfilled

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

X-Ray Specs
^^^^^^^^^^^

Definitions:

* A test that accesses or edits private, internal state of the subject that it shouldn't logically be privy to.

Also Known As:

* 

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Testing many units
------------------

Indirect Testing
^^^^^^^^^^^^^^^^

Definitions:

* The Test Method is interacting with the SUT indirectly via another object thereby making the interactions more complex.

Also Known As:

* 

Code Example::

References:
  * Obscure Test

Test execution / behavior
=========================

Performance
-----------

Asynchronous Test
^^^^^^^^^^^^^^^^^

Definitions:

* A few tests take inordinately long to run
*  those tests contain explicit delays.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Factories pulling too many dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Calling one factory may silently create many associated records, which accumulates to make the whole test suite slow (more on that later)

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns: Fixtures and Factories

Sleeping for arbitrary amount of time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When a test becomes fragile to network or processing congestion

Also Known As:

* 

Code Example::

References:
  * Anti-patterns in test automation

Sleepy Test
^^^^^^^^^^^

Definitions:

* Developers introduce this smell when they need to pause execution of statements in a test method for a certain duration (i.e., simulate an external event) and then continuing with execution. Explicitly causing a thread to sleep can lead to unexpected results as the processing time for a task differs when executed in various environments and configurations.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Sleepy Test
^^^^^^^^^^^

Definitions:

* Explicitly causing a thread to sleep can lead to unexpected results as the processing time for a task can differ on different devices. Developers introduce this smell when they need to pause execution of statements in a test method for a certain duration (i.e. simulate an external event) and then continuing with execution.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Sleepy Test
^^^^^^^^^^^

Definitions:

* Developers introduce this smell when they need to pause execution of statements in a test method for a certain duration (i.e., simulate an external event) and then continuing with execution. Explicitly causing a thread to sleep can lead to unexpected results as the processing time for a task differs when executed in various environments and configurations.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Slow Test
^^^^^^^^^

Definitions:

* Slow tests are kind of tests which take long enough to run

Also Known As:

* 

Code Example::

References:
  * A testing anti-pattern safari

The slow poke
^^^^^^^^^^^^^

Definitions:

* Usually, it puts the test suite to execution and takes longer to finish and give the developer feedback.

Also Known As:

* 

Code Example::

References:
  * TDD anti patterns - Chapter 1

The slow poke
^^^^^^^^^^^^^

Definitions:

* Usually, it puts the test suite to execution and takes longer to finish and give the developer feedback.

Also Known As:

* 

Code Example::

References:
  * TDD anti-patterns - the liar, excessive setup, the giant, slow poke

Other test execution / behavior
-------------------------------

Chatty logging 
^^^^^^^^^^^^^^^

Definitions:

* often a substitute for self-explanatory assertions or well defined test names, the test writes lots of data to the console or logs in order to explain test failures outside of the assertions

Also Known As:

* 

Code Example::

References:
  * Test Smells - The Coding Craftsman

Redundant Print
^^^^^^^^^^^^^^^

Definitions:

* Print statements in unit tests are redundant as unit tests are executed as part of an automated. Furthermore, they can consume computing resources or increase execution time if the developer calls an intensive/long-running method from within the print method (i.e., as a parameter).

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Redundant Print
^^^^^^^^^^^^^^^

Definitions:

* Print statements in unit tests are redundant as unit tests are executed as part of an automated process with little to no human intervention. Print statements are possibly used by developers for traceability and debugging purposes and then forgotten.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Redundant Print
^^^^^^^^^^^^^^^

Definitions:

* Print statements in unit tests are redundant as unit tests are executed as part of an automated. Furthermore, they can consume computing resources or increase execution time if the developer calls an intensive/long-running method from within the print method (i.e., as a parameter).

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Transcripting Test
^^^^^^^^^^^^^^^^^^

Definitions:

* A Transcripting Test is writing information to the console or a global stream, for example the Transcript in Smalltalk, while it is running.

Also Known As:

* 

Code Example::

References:
  * Assessing test quality ‐ TestLint

Unnecessary Navigation
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When the test has actions, taken for granted, not related to the things we want to check

Also Known As:

* 

Code Example::

References:
  * How test automation with selenium can fail

Design related
==============

Not using test patterns
-----------------------

Autogeneration
^^^^^^^^^^^^^^

Definitions:

* Auto-generated tests that test methods instead of behavior

Also Known As:

* 

Code Example::

References:
  * Bad tests, good tests

Constructor Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Ideally, the test suite should not have a constructor. Initialization of fields should be in the setUp() method. Developers who are unaware of the purpose of setUp() method would enable this smell by defining a constructor for the test suite.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Constructor Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Ideally, the test suite should not have a constructor. Initialization of fields should be in the setUp() method. Developers who are unaware of the purpose of setUp() method would give rise to this smell by defining a constructor for the test suite.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Constructor Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Ideally, the test suite should not have a constructor. Initialization of fields should be in the setUp() method. Developers who are unaware of the purpose of setUp() method would enable this smell by defining a constructor for the test suite.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Disorder
^^^^^^^^

Definitions:

* The sequence of elements within a module does not conform to a given order.
A preferred ordering could be:
• imports
• module parameters
• data types
• port types
• component types
• templates
• functions
• altsteps
• test cases
• control part

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Missing Log
^^^^^^^^^^^

Definitions:

* setverdict is used with verdict inconc or fail, but without calling log. Inconclusive or unsuccessful test verdicts should be logged, because this helps discovering the reasons for the failure. However, this smell should be classified weak compared to other smells.

Also Known As:

* 

Code Example::

References:
  * Pattern-based Smell Detection in TTCN-3 Test Suites

Not using page-objects
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Page objects are just a design pattern to ensure automated UI tests use reusable, modular code. Not using them, eg, writing WebDriver code directly in step definitions, means any changes to your UI will require updates in lots of different places instead of the one ‘page’ class.

Also Known As:

* 

Code Example::

References:
  * Five automated acceptance test anti-patterns

Test::class Hierarchy
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* When test classes are not independent and test methods are inherited

Also Known As:

* 

Code Example::

References:
  * Test::Class Hierarchy Is an Antipattern

Unknown Test
^^^^^^^^^^^^

Definitions:

* An assertion statement describes an expected condition for a test method. By examining the assertion statement, it is possible to understand the purpose of the test. However, It is possible for a test method to be written without an assertion statement, in such an instance JUnit will show the test method as passing if the  statements within the test method did not result in a thrown exception when executed.

Also Known As:

* 

Code Example::

References:
  * On the distribution of test smells in open source Android applications: an exploratory study

Unknown Test
^^^^^^^^^^^^

Definitions:

* An assertion statement is used to declare an expected boolean condition for a test method. By examining the assertion statement it is possible to understand the purpose of the test method. However, It is possible for a test method to written sans an assertion statement, in such an instance JUnit will show the test method as passing if the statements within the test method did not result in an exception, when executed. New developers to the project will find it difficult in understanding the purpose of such test methods (more so if the name of the test method is not descriptive enough).

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Unknown Test
^^^^^^^^^^^^

Definitions:

* An assertion statement describes an expected condition for a test method. By examining the assertion statement, it is possible to understand the purpose of the test. However, It is possible for a test method to be written without an assertion statement, in such an instance JUnit will show the test method as passing if the  statements within the test method did not result in a thrown exception when executed.

Also Known As:

* 

Code Example::

References:
  * What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications

Dependencies
============

Dependencies among tests
------------------------

Constrained test order
^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Tests expecting to be run in a specific order or expecting information from other test results

Also Known As:

* 

Code Example::

References:
  * Chapter 8. The pillars of good unit tests

coupling between test methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test methods (and all tests in general) must be perfectly isolated from each other. This means that changing one test must not affect any others.

Also Known As:

* 

Code Example::

References:
  * A few thoughts on unit test scaffolding

Interacting Test Suites
^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A special case of Interacting Tests where the tests are in different test suites.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

Litter Bugs
^^^^^^^^^^^

Definitions:

* Each test has a side effect that persists between test cases, often resulting in tests that depend on one another. This is often called "test pollution"

Also Known As:

* test pollution

Code Example::

References:
  * A workbook repository of example test smells and what to do about them

Order Dependent Tests
^^^^^^^^^^^^^^^^^^^^^

Definitions:

* The tests have to be executed in a certain order due to dependencies between them.

Also Known As:

* 

Code Example::

References:
  * A testing anti-pattern safari

Test Run War
^^^^^^^^^^^^

Definitions:

* Test failures occur at random when several people are running tests simultaneously.

Also Known As:

* 

Code Example::

References:
  * xUnit test patterns: Refactoring test code

External dependencies
---------------------

Factories depending on database records
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Adding a hard dependency on specific database records in factory definitions leads to build failures in CI environment.

Also Known As:

* 

Code Example::

References:
  * Rails Testing Antipatterns: Fixtures and Factories

Hidden Integration Test
^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* A PUT outcome depends on the state of the environment.

Also Known As:

* 

Code Example::

References:
  * Parameterized Test Patterns For Effective Testing with Pex

Mystery Guest
^^^^^^^^^^^^^

Definitions:

* A test case that uses external resources that are not managed by a fixture. A drawback of this approach is that the interface to external resources might change over time necessitating an update of the test case, or that those resources might not be available when the test case is run, endangering the deterministic behavior of the test.

Also Known As:

* 

Code Example::

References:
  * Assessing diffusion and perception of test smells in scala projects

Mystery Guest
^^^^^^^^^^^^^

Definitions:

* The test reader is not able to see the cause and effect between fixture and verification logic because part of it is done outside the Test Method.

Also Known As:

* 

Code Example::

References:
  * Let’s not

Mystery Guest
^^^^^^^^^^^^^

Definitions:

* The test reader is not able to see the cause and effect between fixture and verification logic because part of it is done outside the Test Method.

Also Known As:

* 

Code Example::

References:
  * Mystery Guest

Mystery Guest
^^^^^^^^^^^^^

Definitions:

* The test reader is not able to see the cause and effect between fixture and verification logic because part of it is done outside the Test Method.

Also Known As:

* 

Code Example::

References:
  * Obscure Test

Mystery Guest
^^^^^^^^^^^^^

Definitions:

* Occurs when a test method utilizes external resources (e.g. files, database, etc.). Use of external resources in test methods will result in stability and performance issues. Developers should use mock objects in place of external resources.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

Require External Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^

Definitions:

* Test require external resources but can not guarantee their state and availability

Also Known As:

* 

Code Example::

References:
  * A testing anti-pattern safari

Resource Optimism
^^^^^^^^^^^^^^^^^

Definitions:

* This smell happens when test methods make optimistic assumptions about the existence or the state of external resources like files and databases.

Also Known As:

* 

Code Example::

References:
  * Refactoring Test Smells: A Perspective from Open-Source Developers

Resource Optimism
^^^^^^^^^^^^^^^^^

Definitions:

* This smell occurs when a test method makes an optimistic assumption that the external resource (e.g., File), utilized by the test method, exists.

Also Known As:

* 

Code Example::

References:
  * Software Unit Test Smells

NONE
====

NONE
----

Messy Test
^^^^^^^^^^

Definitions:

* Tests that contain repeated code, copy&paste, disorganized structure and literal values

Also Known As:

* 

Code Example::

References:
  * A testing anti-pattern safari

