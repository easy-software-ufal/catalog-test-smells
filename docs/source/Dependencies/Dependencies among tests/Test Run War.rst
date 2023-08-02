Test Run War
^^^^^
**Definition:**

* Test failures occur at random when several people are running tests simultaneously.


**Code Example:**

.. code-block:: ruby

  Suite.run() --> Test 3 fails
  Suite.run() --> Test 3 crashes
  Suite.run() --> All tests pass
  Suite.run() --> Test 3 fails

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `A survey on test practitioners' awareness of test smells <https://arxiv.org/abs/2003.05613>`_
* `An empirical analysis of the distribution of unit test smells and their impact on software maintenance <https://ieeexplore.ieee.org/document/6405253>`_ :octicon:`graph;1em`
* `An exploratory study of the relationship between software test smells and fault-proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
* `Are test smells really harmful? An empirical study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Automatic generation of smell-free unit tests <https://repositorio.ul.pt/handle/10451/56819>`_ :octicon:`comment-discussion;1em`
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `Enhancing developers’ awareness on test suites’ quality with test smell summaries <https://lutpub.lut.fi/handle/10024/158751>`_
* `How are test smells treated in the wild? A tale of two empirical studies <https://sol.sbc.org.br/journals/index.php/jserd/article/download/1802/1807/7485>`_ :octicon:`graph;1em`
* `On the interplay between software testing and evolution and its effect on program comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
* `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `Refactoring Test Smells With JUnit 5: Why Should Developers Keep Up-to-Date? <https://ieeexplore.ieee.org/document/9769994/>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`graph;1em` :octicon:`sync;1em`
* `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
* `Understanding practitioners’ strategies to handle test smells: a multi-method study <https://dl.acm.org/doi/10.1145/3474624.3474639>`_ :octicon:`comment-discussion;1em` :octicon:`sync;1em`
* `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em` :octicon:`sync;1em`
