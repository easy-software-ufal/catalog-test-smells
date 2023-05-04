Resource Optimism
^^^^^
Definitions:

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

 * `Refactoring Test Smells: A Perspective from Open-Source Developers <https://dl.acm.org/doi/10.1145/3425174.3425212>`_
 * `Software Unit Test Smells <https://testsmells.org/>`_

