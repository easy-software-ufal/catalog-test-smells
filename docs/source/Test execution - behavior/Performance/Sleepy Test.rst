Sleepy Test
^^^^^
Definition:

* Developers introduce this smell when they need to pause execution of statements in a test method for a certain duration (i.e., simulate an external event) and then continuing with execution. Explicitly causing a thread to sleep can lead to unexpected results as the processing time for a task differs when executed in various environments and configurations.


Code Example:

.. code-block:: java

    public void testEdictExternSearch() throws Exception {
        final Intent i = new Intent(getInstrumentation().getContext(), ResultActivity.class);
        i.setAction(ResultActivity.EDICT_ACTION_INTERCEPT);
        i.putExtra(ResultActivity.EDICT_INTENTKEY_KANJIS, "空白");
        tester.startActivity(i);
        assertTrue(tester.getText(R.id.textSelectedDictionary).contains("Default"));
        final ListView lv = getActivity().getListView();
        assertEquals(1, lv.getCount());
        DictEntry entry = (DictEntry) lv.getItemAtPosition(0);
        assertEquals("Searching", entry.english);
        Thread.sleep(500);
        final Intent i2 = getStartedActivityIntent();
        final List result = (List) i2.getSerializableExtra(ResultActivity.INTENTKEY_RESULT_LIST);
        entry = result.get(0);
        assertEquals("(adj-na,n,adj-no) blank space/vacuum/space/null (NUL)/(P)", entry.english);
        assertEquals("空白", entry.getJapanese());
        assertEquals("くうはく", entry.reading);
        assertEquals(1, result.size());
    }

References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
 * `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`file-code;1em` :octicon:`graph;1em`
 * `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
 * `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
 * `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_
 * `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
 * `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
 * `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
 * `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `PyNose: A Test Smell Detector For Python <https://ieeexplore.ieee.org/document/9678615/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
 * `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_

