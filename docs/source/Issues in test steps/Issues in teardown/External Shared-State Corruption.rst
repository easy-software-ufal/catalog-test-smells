External Shared-State Corruption
^^^^^
**Definition:**

* Integration tests with shared resources and no rollback


**Code Example:**

.. code-block:: text

  Similar to shared-state corruption.
  Tests touch shared resources (either in memory or in external resources,such as databases and filesystems)
  without cleaning up or rolling back any changes they make to those resources.

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency

* `Chapter 8. The pillars of good unit tests <https://apprize.best/c/unit/8.html>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`

