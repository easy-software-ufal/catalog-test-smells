Erratic Tests
^^^^^
Definition:

* Tests that will pass or fail without you changing anything


Code Example:

.. code-block:: javascript

  first(".active").click

  all(".active").each(&:click)

  execute_script("$('.active').focus()")

  expect(find_field("Username").value).to eq("Joe")

  expect(find(".user")["data-name"]).to eq("Joe")

  expect(has_css?(".active")).to eq(false)

References:

 * `Rails Testing Antipatterns <https://thoughtbot.com/upcase/videos/testing-antipatterns>`_ :octicon:`file-code;1em`

