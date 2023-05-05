The Slow Poke
^^^^^
Definitions:

* Usually, it puts the test suite to execution and takes longer to finish and give the developer feedback.


Code Example:

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


References:

 * `TDD anti patterns - Chapter 1 <https://www.codurance.com/publications/tdd-anti-patterns-chapter-1>`_
 * `TDD anti-patterns - the liar, excessive setup, the giant, slow poke <https://marabesi.com/tdd/2021/08/28/tdd-anti-patterns.html>`_

