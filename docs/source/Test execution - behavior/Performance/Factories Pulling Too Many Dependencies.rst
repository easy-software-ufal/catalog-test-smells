Factories Pulling Too Many Dependencies
^^^^^
Definitions:

* Calling one factory may silently create many associated records, which accumulates to make the whole test suite slow (more on that later)


Code Example::

References:

 * `Rails Testing Antipatterns: Fixtures and Factories <https://semaphoreci.com/blog/2014/01/14/rails-testing-antipatterns-fixtures-and-factories.html>`_
