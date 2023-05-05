Overspecified Tests
^^^^^
Definition:

* Tests that specify too many things that aren’t genuinely related to the scenario being tested.


Code Example:

.. code-block:: java

  @Mock private DataSource dataSource;
  @Mock private Mock connection;
  @Mock private Mock statement;
  @Mock private ResultSet resultSet;
  @Test
  public void test() throws Exception {
    MockitoAnnotations.initMocks(this);
    systemUnderTest = new OracleDAOImpl();
    systemUnderTest.setDBConnectionManager(connectionManager);
    Set<NACustomerDTO> set = new HashSet<NACustomerDTO>();
    when(connectionManager.getDataSource()).thenReturn(dataSource);
    when(dataSource.getConnection()).thenReturn(connection);
    when(connection.createStatement()).thenReturn(statement);
    when(statement.executeQuery(anyString())).thenReturn(resultSet);
    when(resultSet.next()).thenReturn(false);
    when(resultSet.getLong(1)).thenReturn(1L);
    when(resultSet.getString(2)).thenReturn("7178");
    doNothing().when(resultSet).close();
    stub(systemUnderTest.getNACustomers()).toReturn(set); 
    final Set<NACustomerDTO> result = systemUnderTest.getNACustomers();
    verify(connectionManager).getDataSource();
    verify(dataSource).getConnection();
    verify(connection).createStatement();
    verify(statement).executeQuery(anyString());
    verify(resultSet).next();
    verify(resultSet).getLong(1);
    verify(resultSet).getString(2);
    assertNotNull(result); 
    verify(connectionManager).getDataSource().getConnection();
  }


References:

 * `Bad tests, good tests <http://kaczanowscy.pl/books/bad_tests_good_tests.html>`_

