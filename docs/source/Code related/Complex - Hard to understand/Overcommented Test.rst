Overcommented Test
^^^^^
**Definition:**

* Overcommented Tests dene too many comments, obfuscating the code and distracting from the purpose of the test.


**Code Example:**

.. code-block:: go

  DebuggerTest >> #testUnwindDebuggerWithStep
    "test if unwind blocks work properly when a debugger is closed"
    | sema process debugger top |
    sema := Semaphore forMutualExclusion.
    self assert: sema isSignaled.
    process := [sema critical:[sema wait]]
    forkAt: Processor userInterruptPriority.
    self deny: sema isSignaled.
    "everything set up here - open a debug notifier"
    debugger := Debugger openInterrupt: ’test’ onProcess: process.
    "get into the debugger"
    debugger debug.
    top := debugger topView.
    "set top context"
    debugger toggleContextStackIndex: 1.
    "do single step"
    debugger doStep.
    "close debugger"
    top delete.
    "and see if unwind protection worked"
    self assert: sema isSignaled

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Assessing test quality ‐ TestLint <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.144.9594>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Rule-Based Assessment of Test Quality <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.3631&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_

