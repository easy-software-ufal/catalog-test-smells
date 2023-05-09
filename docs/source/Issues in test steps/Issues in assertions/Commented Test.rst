Commented Test
^^^^^
Definition:

* Test contents are commented so that it passes


Code Example:

.. code-block:: java

  class SystemAdminSmokeTest extends GroovyTestCase {
    void testSmoke() {
      // do not remove below code
      // def ds = new org.h2.jdbcx.JdbcDataSource(
      // URL: 'jdbc:h2:mem:test;DB_CLOSE_DELAY=-1;MODE=Oracle',
      // user: 'sa', password: '')
      //
      // def jpaProperties = new Properties()
      // jpaProperties.setProperty(
      // 'hibernate.cache.use_second_level_cache', 'false')
      // jpaProperties.setProperty(
      // 'hibernate.cache.use_query_cache', 'false')
      //
      // def emf = new LocalContainerEntityManagerFactoryBean(
      // dataSource: ds, persistenceUnitName: 'my-domain',
      // jpaVendorAdapter: new HibernateJpaVendorAdapter(
      // database: Database.H2, showSql: true,
      // generateDdl: true), jpaProperties: jpaProperties)
      ...
    }
  }


References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

