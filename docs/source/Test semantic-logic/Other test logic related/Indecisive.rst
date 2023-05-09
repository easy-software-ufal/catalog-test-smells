Indecisive
^^^^^
Definition:

* A test contains branching logic. Of course, test-scoped logic is always risky, since it is itself untested. But this smell portends some deeper issues worth discussing.


Code Example:

.. code-block:: ruby

  # Subject under test
  require 'rbconfig'

  def join_path(fragments)
    if /mswin/ =~ RbConfig::CONFIG['host_os']
      separator = "\\"
      pattern = /\\+/
    else
      separator = "/"
      pattern = /\/+/
    end
    fragments.join(separator).gsub(pattern, separator)
  end

  # Test
  class Indecisive < SmellTest
    def test_simple_case
      fragments = ["foo", "bar", "baz"]

      result = join_path(fragments)

      if /mswin/ =~ RbConfig::CONFIG['host_os']
        assert_equal "foo\\bar\\baz", result
      else
        assert_equal "foo/bar/baz", result
      end
    end

    def test_contains_separators
      if /mswin/ =~ RbConfig::CONFIG['host_os']
        fragments = ["\\foo\\", "bar\\biz", "baz\\"]
      else
        fragments = ["/foo/", "bar/biz", "baz/"]
      end

      result = join_path(fragments)

      if /mswin/ =~ RbConfig::CONFIG['host_os']
        assert_equal "\\foo\\bar\\biz\\baz\\", result
      else
        assert_equal "/foo/bar/biz/baz/", result
      end
    end
  end

References

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `A workbook repository of example test smells and what to do about them <https://github.com/testdouble/test-smells>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

