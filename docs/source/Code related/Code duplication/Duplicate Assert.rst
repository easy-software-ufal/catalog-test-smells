Duplicate Assert
^^^^^
**Definition:**

* This smell occurs when a test method tests for the same condition multiple times within the same test method. If the test method needs to test the same condition using different values, a new test method should be created. As a best practice, the name of the test method should be an indication of the test being performed. Possible situations that would give rise to this smell include (1) developers grouping multiple conditions to test a single method, (2) developers performing debugging activities, and (3) an accidental copy-paste of code


**Code Example:**

.. code-block:: java

    @Test
    public void testXmlSanitizer() {
        boolean valid = XmlSanitizer.isValid("Fritzbox");
        assertEquals("Fritzbox is valid", true, valid);
        System.out.println("Pure ASCII test - passed");

        valid = XmlSanitizer.isValid("Fritz Box");
        assertEquals("Spaces are valid", true, valid);
        System.out.println("Spaces test - passed");

        valid = XmlSanitizer.isValid("Frützbüx");
        assertEquals("Frützbüx is invalid", false, valid);
        System.out.println("No ASCII test - passed");

        valid = XmlSanitizer.isValid("Fritz!box");
        assertEquals("Exclamation mark is valid", true, valid);
        System.out.println("Exclamation mark test - passed");

        valid = XmlSanitizer.isValid("Fritz.box");
        assertEquals("Exclamation mark is valid", true, valid);
        System.out.println("Dot test - passed");

        valid = XmlSanitizer.isValid("Fritz-box");
        assertEquals("Minus is valid", true, valid);
        System.out.println("Minus test - passed");

        valid = XmlSanitizer.isValid("Fritz-box");
        assertEquals("Minus is valid", true, valid);
        System.out.println("Minus test - passed");
    }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
* `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
* `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
* `On the distribution of test smells in open source Android applications: an exploratory study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
* `On the influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the use of test smells for prediction of flaky tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `RAIDE: a tool for Assertion Roulette and Duplicate Assert identification and refactoring <https://dl.acm.org/doi/10.1145/3422392.3422510>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `The secret life of test smells-an empirical study on test smell evolution and maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
* `tsDetect: an open source test smells detection tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
* `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
