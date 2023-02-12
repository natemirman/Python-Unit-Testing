from invoice import Invoice, Item


def test_invoice_initializes_name(name: str = "John Doe") -> tuple[bool, str]:
    """
    Tests that a new Invoice object is initialized with the correct name.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    invoice = Invoice(name)

    fail_case = invoice.client_name != name

    if fail_case:
        return (False, f"Error in test_invoice_initializes_name: Incorrect name\n  - Expected: {name}\n  - Actual: {invoice.client_name}")
    else:
        return (True, "Invoice object name correctly initialized")


def test_invoice_initializes_date(date: str = "2021-09-01") -> tuple[bool, str]:
    """
    Tests that a new Invoice object is initialized with the correct date.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    invoice = Invoice("John Doe", date)

    fail_case = invoice.date != date

    if fail_case:
        return (False, f"Error in test_invoice_initializes_date: Incorrect date\n  - Expected: {date}\n  - Actual: {invoice.date}")
    else:
        return (True, "Invoice object date correctly initialized")


def test_invoice_initializes_discounted_false() -> tuple[bool, str]:
    """
    Tests that a new Invoice object is initialized with a discounted value of False when no value is provided.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    invoice = Invoice("John Doe")

    fail_case = invoice.discounted != False

    if fail_case:
        return (False, f"Error in test_invoice_initializes_discounted_false: Incorrect discounted value\n  - Expected: False\n  - Actual: {invoice.discounted}")
    else:
        return (True, "Invoice object discounted correctly initialized")


def test_invoice_initializes_discounted_true() -> tuple[bool, str]:
    """
    Tests that a new Invoice object is initialized with a discounted value of True when True is provided.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    invoice = Invoice("John Doe", "2021-09-01", True)

    fail_case = invoice.discounted != True

    if fail_case:
        return (False, f"Error in test_invoice_initializes_discounted_true: Incorrect discounted value\n  - Expected: True\n  - Actual: {invoice.discounted}")
    else:
        return (True, "Invoice object discounted correctly initialized")


def test_invoice_add_item_appends_item() -> tuple[bool, str]:
    """
    Tests that the Invoice.add_item method appends the given item to the invoice's items list.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    # TODO 4: Implement this test
    # - Create a new Invoice object
    # - Create a new Item object and add it to the invoice
    # - Check that the item inside the invoice.items list is the same as the item you created
    # - Run the test before implementing the Invoice.add_item method and check that it fails
    invoice = Invoice("Nate Mirman","2022-02-08",True)  # Replace None with the correct code
    item = Item("test item", 1, 1.0, .02)
    invoice.add_item(item.name,item.quantity,item.unit_price,item.discount_percent)
    expected = None
    try:
        fail_case=invoice.items[0].name != item.name
        actual = invoice.items[0].name
    except:
        fail_case=True
        actual = "N/A"

    if fail_case:
        return (False, f"Error in test_invoice_add_item_appends_item: Incorrect item\n  - Expected: {expected}\n  - Actual: {actual}")
    else:
        return (True, "Invoice.add_item method correctly appends the given item to the invoice's items list")


def test_invoice_add_item_checks_discounted() -> tuple[bool, str]:
    """
    Tests that the Invoice.add_item method checks if the invoice is discounted.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    # TODO 5: Implement this test
    # - Create a new Invoice object with a discounted value of True
    # - Create a new Item object and add it to the invoice
    # - Check that the item inside the invoice.items list has the expected discount percent
    # - Run the test before implementing the Invoice.add_item method and check that it fails

    invoice = Invoice("Nate Mirman","2022-02-08",True)  # Replace None with the correct code
    item = Item("test item", 1, 1.0, .02) # Replace None with the correct code
                                         # Replace True with the correct code
    expected = .02  # Replace None with the correct code
    invoice.add_item(item.name,item.quantity,item.unit_price,item.discount_percent) # Replace None with the correct code

    try:
        fail_case=invoice.items[0].discount_percent != item.discount_percent
        actual = invoice.items[0].discount_percent
    except:
        fail_case=True
        actual = -1

    if fail_case:
        return (False, f"Error in test_invoice_add_item_checks_discounted: Incorrect discount percent\n  - Expected: {expected}\n  - Actual: {actual}")
    else:
        return (True, "Invoice.add_item method correctly checks if the invoice is discounted")
