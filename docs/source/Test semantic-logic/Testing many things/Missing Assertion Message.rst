Missing Assertion Message
^^^^^
Definition:

* A test fails. Upon examining the output of the Test Runner, we cannot determine exactly which assertion had failed.


Code Example:

.. code-block:: java
    
    public void testInvoice_addLineItem7() {
        LineItem expItem = new LineItem(inv, product, QUANTITY);
        //  Exercise
        inv.addItemQuantity(product, QUANTITY);
        // Verify
        List lineItems = inv.getLineItems();
        LineItem actual = (LineItem)lineItems.get(0);
        assertEquals(expItem.getInv(), actual.getInv());
        assertEquals(expItem.getProd(), actual.getProd());
        assertEquals(expItem.getQuantity(), actual.getQuantity());
    }  

References:

 * `xUnit Test Patterns: Refactoring Test Code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_
 * `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_

