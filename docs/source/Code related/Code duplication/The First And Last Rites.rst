The First And Last Rites 
^^^^^
Definition:

* Where there’s some ritual/boilerplate at the start and end of most test bodies, suggesting a lack of common setup/teardown code

Also Known As:

* Oops I Forgot The Setup

Code Example:

.. code-block:: java

    @Test
    public void connectionWorks() {
        database = openDatabase();
    
        database.healthCheck();
    
        database.close();
    }
    
    @Test
    public void countRows() {
        database = openDatabase();
    
        assertThat(database.countAll())
        .isEqualTo(0);
    
        database.close();
    }

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

