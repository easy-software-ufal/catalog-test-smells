The Slow Poke
^^^^^
**Definition:**

* Usually, it puts the test suite to execution and takes longer to finish and give the developer feedback.

**Also Known As:**

* Slow Test

**Code Example:**

.. code-block:: javascript

    test('shoutd show Buggy on user interaction by keyboard', done => {
        const wrapper = mount(
        <Guide 
            guideContent={content}
            currentHint={0}
            showNext={false}
            invalidCode={false}
            afkExpirationTime={ 400}
            />
        );

    setTimeout(() => {
        wrapper .update();
        expect (wrapper.find('BuggySleepy'). length).toBe(1);
    }


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `TDD anti patterns - Chapter 1 <https://www.codurance.com/publications/tdd-anti-patterns-chapter-1>`_ :octicon:`file-code;1em`
* `TDD anti-patterns - the liar, excessive setup, the giant, slow poke <https://marabesi.com/tdd/2021/08/28/tdd-anti-patterns.html>`_ :octicon:`file-code;1em`
* `Test-Driven Development: TDD Anti-Patterns <https://bryanwilhite.github.io/the-funky-knowledge-base/entry/kb2076072213/>`_
* `Unit Testing Anti-Patterns, Full List <https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html>`_
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_
