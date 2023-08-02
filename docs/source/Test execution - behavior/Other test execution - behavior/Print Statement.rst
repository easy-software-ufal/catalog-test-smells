Print Statement
^^^^^
**Definition:**

* Print statements in unit tests are redundant as unit tests are executed as part of an automated script and do not affect the failing or passing of test cases. Furthermore, they can increase execution time if the developer calls a long-running method from within the print method (i.e., as a parameter).


**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Automatic Identification of High-Impact Bug Report by Product and Test Code Quality <https://huang.zj.cn/pdf/J13.pdf>`_
* `On the diffusion of test smells and their relationship with test code quality of Java projects <https://onlinelibrary.wiley.com/doi/abs/10.1002/smr.2532>`_ :octicon:`graph;1em`
* `On the influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
* `On the test smells detection: an empirical study on the jnose test accuracy <https://sol.sbc.org.br/journals/index.php/jserd/article/view/1893>`_ :octicon:`graph;1em`
* `The secret life of test smells-an empirical study on test smell evolution and maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
