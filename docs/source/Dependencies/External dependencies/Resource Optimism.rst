Resource Optimism
^^^^^
Definition:

* This smell happens when test methods make optimistic assumptions about the existence or the state of external resources like files and databases.
* This smell occurs when a test method makes an optimistic assumption that the external resource (e.g., File), utilized by the test method, exists.


Code Example:

.. code-block:: java

  @Test
  public void saveImage_noImageFile_ko() throws IOException {
    File outputFile = File.createTempFile("prefix", "png", new File("/tmp"));
    ProductImage image = new ProductImage("01010101010101", ProductImageField.FRONT, outputFile);
    Response response = serviceWrite.saveImage(image.getCode(), image.getField(), image.getImguploadFront(), image.getImguploadIngredients(), image.getImguploadNutrition()).execute();
    assertTrue(response.isSuccess());
    assertThatJson(response.body())
        .node("status")
            .isEqualTo("status not ok");
  }

References:
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_ :octicon:`file-code;1em`
 * `Software Unit Test Smells <https://testsmells.org/>`_ :octicon:`file-code;1em`
 * `A Survey on Test Practitioners' Awareness of Test Smells <https://arxiv.org/abs/2003.05613>`_
 * `An Empirical Analysis of the Distribution of Unit Test Smells and Their Impact on Software Maintenance <https://ieeexplore.ieee.org/document/6405253>`_
 * `An Exploratory Study of the Relationship Between Software Test Smells and Fault-Proneness <https://ieeexplore.ieee.org/abstract/document/8847402/>`_ :octicon:`graph;1em`
 * `An Exploratory Study on the Refactoring of Unit Test Files in Android Applications <https://dl.acm.org/doi/10.1145/3387940.3392189>`_
 * `Are Test Smells Really Harmful? An Empirical Study <https://link.springer.com/article/10.1007/s10664-014-9313-0>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
 * `Enhancing Developers’ Awareness on Test Suites’ Quality With Test Smell Summaries <https://lutpub.lut.fi/handle/10024/158751>`_
 * `Handling Test Smells in Python: Results from a Mixed-Method Study <https://dl.acm.org/doi/10.1145/3474624.3477066>`_
 * `Investigating Severity Thresholds for Test Smells <https://dl.acm.org/doi/abs/10.1145/3379597.3387453>`_
 * `Investigating Test Smells in JavaScript Test Code <https://dl.acm.org/doi/10.1145/3482909.3482915>`_ :octicon:`graph;1em`
 * `On the Diffusion of Test Smells in Automatically Generated Test Code: An Empirical Study <https://dl.acm.org/doi/10.1145/2897010.2897016>`_
 * `On the Distribution of "Simple Stupid Bugs" in Unit Test Files: An Exploratory Study <https://ieeexplore.ieee.org/document/9463091>`_
 * `On the Distribution of Test Smells in Open Source Android Applications: An Exploratory Study <https://dl.acm.org/doi/10.5555/3370272.3370293>`_ :octicon:`graph;1em`
 * `On the Influence of Test Smells on Test Coverage <https://dl.acm.org/doi/10.1145/3350768.3350775>`_
 * `On the Interplay Between Software Testing and Evolution and Its Effect on Program Comprehension <https://link.springer.com/chapter/10.1007/978-3-540-76440-3_8>`_ :octicon:`comment-discussion;1em`
 * `On the Relation of Test Smells to Software Code Quality <https://ieeexplore.ieee.org/document/8529832>`_
 * `On the Use of Test Smells for Prediction of Flaky Tests <https://dl.acm.org/doi/abs/10.1145/3482909.3482916>`_ :octicon:`comment-discussion;1em` :octicon:`graph;1em`
 * `Refactoring Test Code <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.5499&rep=rep1&type=pdf>`_ :octicon:`comment-discussion;1em`
 * `Revisiting Test Smells in Automatically Generated Tests: Limitations, Pitfalls, and Opportunities <https://ieeexplore.ieee.org/document/9240691>`_ :octicon:`graph;1em`
 * `Scented Since the Beginning: On the Diffuseness of Test Smells in Automatically Generated Test Code <https://www.sciencedirect.com/science/article/pii/S0164121219301487?casa_token=UT0EMFzxTcQAAAAA:L9J82_15tdySkabcIMSHKPx8rVkrltOzcwgme5cIBWgT0txJENY5y-BdUmCYUoGHnoEjZJH-cYc>`_
 * `Test Smell Detection Tools: A Systematic Mapping Study <https://dl.acm.org/doi/10.1145/3463274.3463335>`_
 * `The Relation of Test-Related Factors to Software Quality: A Case Study on Apache Systems <https://search.proquest.com/openview/c52d821a4dd6ecb046957d9d6a532ae0/1?pq-origsite=gscholar&cbl=326341>`_ :octicon:`graph;1em`
 * `The Secret Life of Test Smells - An Empirical Study on Test Smell Evolution and Maintenance <https://link.springer.com/article/10.1007/s10664-021-09969-1>`_ :octicon:`graph;1em`
 * `Toward Static Test Flakiness Prediction: A Feasibility Study <https://dl.acm.org/doi/10.1145/3472674.3473981>`_ :octicon:`graph;1em`
 * `tsDetect: An Open Source Test Smells Detection Tool <https://dl.acm.org/doi/10.1145/3368089.3417921>`_
 * `What the Smell? An Empirical Investigation on the Distribution and Severity of Test Smells in Open Source Android Applications <https://www.proquest.com/openview/17433ac63caf619abb410e441e6557f0/1?pq-origsite=gscholar&cbl=18750>`_ :octicon:`graph;1em`
 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`comment-discussion;1em`

