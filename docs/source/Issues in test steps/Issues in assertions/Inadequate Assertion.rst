Inadequate Assertion
^^^^^
**Definition:**

* Every update to the execution state must eventually be verified in the assertions. In principle, assertions should verify the correctness of all updates to the  object/program state, otherwise the strength of the test oracles is considered not enough to guard the program against faults.


**Code Example:**

.. code-block:: java

    public class ClassUnderTest{
        private int data1;
        private int data2;
        public int getData1() { return data1;}
        public int getData2() { return data2;}

        public void method1(int flag){
            if(flag>0){
                this.data2 =  2; //define data2
            }
            this.data1 = 4;      //define data1


    public class ClassUnderTest extends TestCase{
        public void testMethod1(){
            ClassUnderTest cut = new ClassUnderTest;
            int testInput = 1;
            cut.method1(testInput);

            assertTrue(cut.getData1()==4); // Is this assertion adequate enough?

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `On adequacy of assertions in automated test suites: an empirical investigation <https://ieeexplore.ieee.org/abstract/document/6571656>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em`
