Duplicate Assert
^^^^^
Definition:

* This smell occurs when a test method tests for the same condition multiple times within the same test method. If the test method needs to test the same condition using different values, a new test method should be created. As a best practice, the name of the test method should be an indication of the test being performed. Possible situations that would give rise to this smell include (1) developers grouping multiple conditions to test a single method, (2) developers performing debugging activities, and (3) an accidental copy-paste of code


Code Example:

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


References:

 * `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_
 * `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
 * `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
 * `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_
 * `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
 * `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
 * `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_
 * `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_
 * `RAIDE: a tool for Assertion Roulette and Duplicate Assert identification and refactoring <https://dl.acm.org/doi/10.1145/3422392.3422510>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_
 * `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_

