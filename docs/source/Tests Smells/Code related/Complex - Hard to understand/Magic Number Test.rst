Magic Number Test
^^^^^
Definitions:

* This smell occurs when a test method contains unexplained and undocumented numeric literals as parameters or as values to identifiers. These magic values do not sufficiently indicate the meaning/purpose of the number. Hence, they hinder code understandability. Consequently, they should be replaced with constants or  variables, thereby providing a descriptive name for the value.
* Occurs when the test method contains undocumented numeric literals with no clear meaning (magic values).
* Occurs when assert statements in a test method contain numeric literals (i.e., magic numbers) as parameters. Magic numbers do not indicate the meaning/purpose of the number. Hence, they should be replaced with constants or variables, thereby providing a descriptive name for the input.
* This smell occurs when a test method contains unexplained and undocumented numeric literals as parameters or as values to identifiers. These magic values do not sufficiently indicate the meaning/purpose of the number. Hence, they hinder code understandability. Consequently, they should be replaced with constants or  variables, thereby providing a descriptive name for the value.


Code Example::

References:

 * `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_

