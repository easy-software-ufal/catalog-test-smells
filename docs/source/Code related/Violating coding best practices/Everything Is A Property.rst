Everything Is A Property
^^^^^
Definitions:

* Where a test class keeps what should be temporary variables in instance variables

Also Known As:

* Temporary Test Property

Code Example:

.. code-block:: java

    class ParagraphAnalyzerTest {
        private String analyzed;
        private ParagraphAnalyzer analyzer = new ParagraphAnalyzer();
    
        @Test
        void nouns() {
            analyzed = analyzer.justNouns("This is a word");
            assertThat(analyzed).isEqualTo("word");
        }
    
        @Test
        void verbs() {
            analyzed = analyzer.justVerbs("This is a word");
            assertThat(analyzed).isEqualTo("is");
        }
    
        @Test
        void ends() {
            analyzed = analyzer.first("This is a word");
            assertThat(analyzed).isEqualTo("This");
    
            analyzed = analyzer.last("This is a word");
            assertThat(analyzed).isEqualTo("words");
        }
    }

References:

 * `Test Smells - The Coding Craftsman <https://codingcraftsman.wordpress.com/2018/09/27/test-smells/>`_

