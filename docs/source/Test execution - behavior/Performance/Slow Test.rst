Slow Test
^^^^^
Definition:

* Slow tests are kind of tests which take long enough to run


Also Known As:

* Long Running Test, The Slow Poke


Code Example:

.. code-block:: ruby
  
  class SlowTest < Test::Unit::TestCase
    def test_fast
      assert true
    end

    def test_slow
      MyClass.slow_method
      assert true
    end
  end

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `A testing anti-pattern safari <https://www.youtube.com/watch?v=VBgySRk0VKY>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
 * `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_ :octicon:`graph;1em`
 * `Investigating into Automated Test Patterns in Erratic Tests by Considering Complex Objects <http://j.mecs-press.net/ijitcs/ijitcs-v7-n3/IJITCS-V7-N3-8.pdf>`_ :octicon:`comment-discussion;1em`
 * `What We Know About Smells in Software Test Code <https://ieeexplore.ieee.org/document/8501942>`_
 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_ :octicon:`comment-discussion;1em`

