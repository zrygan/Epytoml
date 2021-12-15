Notaker
=======

.. Notaker:

What is Notaker?
----------------
| Notaker is an note-taking formatter for python.
| Uses python syntax, and exports your Notaker document in html or pdf formats.

Using Notaker
-------------

| First importing Notaker

.. code-block:: python

    from Epytoml.Notaker import Notaker

| Begin all Notaker documents with the following lines.

.. code-block:: python

    Notaker.ntkGen("yourDocumentName")

    Notaker.makeTitle(1:[FirstName, SurName]}, {"month": "monthCreated", "day": "dayCreated", "year": "yearCreated"})

| Remember to end all Notaker documents with the following lines.

.. code-block:: python

    headerClass().toc()

    Notaker.ntkShut()

Notaker Syntax
--------------

**ntkGen(fileName)**::

    Writes all the document type declaration, html document start, html head, and html body.
    
    Args:
        fileName (str): This is will be the file name of your document.

**ntkShut()**::
    
    Writes html document end, and html head end. Always end your Epytoml code with this.

**nl(lines=None)**::

    Creates one or multiple line breaks.
    
    Args:
        lines (int): Specifies how many line breaks are to be created, if lines is not given a value, this function will only create one line.

**nl(lines=None)**::

    Creates one or multiple line breaks.
    
    Args:
        lines (int): Specifies how many line breaks are to be created, if lines is not given a value, this function will only create one line.

**headerClass**::

    Contains all the functions needed in creating main headers (h1), creating hyperlinks and hyperlink ids, and adding the table of contents.

**headerClass().h(self, content)**::

    Creates a main header (or h1 in html).
    
    Args:
        content (str): This is the text the header will display.
    
    Returns:
        This returns the complete (formatted) main header in html format.

**headerClass().makeLink(self, content, autoFormat=None)**::

    Creates a hyperlink, to be used in the toc function.
    
    Args:
        content (str): This will be set as the hyperlink URL address.
        autoFormat (bool, optional): The makeLink function automatically adds 'Chapter N:' before the content. Defaults to True.
    
    Returns:
        This returns the complete (formatted) hyperlink in html format.

**headerClass().makeId(self, content)**::

    Creates an id attribute. Always add this function every h function call.
    
    Args:
        content (str): This will be set as the hyperlink URL address.
    
    Returns:
        This returns the complete (formatted) id in html format.

**headerClass().headCountAdd(self)**::    

    Increments the ntk_heads variable.

**headerClass().toc(self, size=None)**::

    Creates the table of contents.
    
    Args:
        size (int, optional): This is the size of the table of contents. Defaults to None.
    
**hh(content)**::

    Creates a 2nd subheader (or h2 in html).
    
    Args:
        content (str): This is the text the header will display.
    
    Returns:
        This returns the complete (formatted) main header in html format.

**h3(content)**::

    Creates a 3rd subheader (or h3 in html).
    
    Args:
        content (str): This is the text the header will display.
    
    Returns:
        This returns the complete (formatted) main header in html format.

**h4(content)**::

    Creates a 4th subheader (or h4 in html).
    
    Args:
        content (str): This is the text the header will display.
    
    Returns:
        This returns the complete (formatted) main header in html format.

**h5(content)**::

    Creates a 5th subheader (or h5 in html).
    
    Args:
        content (str): This is the text the header will display.
    
    Returns:
        This returns the complete (formatted) main header in html format.

**h6(content)**::

    Creates a 6th subheader (or h6 in html).
    
    Args:
        content (str): This is the text the header will display.
    
    Returns:
        This returns the complete (formatted) main header in html format.

**t(content, emphasis=None)**::

    Creates normal text in the Notaker document (or p in html).
    
    Args:
        content (str): This is the text the t function will display.
        emphasis (str, optional): Adds text emphasis to the content. Defaults to None.
    
    Returns:
        This returns the complete (formatted) text in html format.

**tL(content, emphasis=None)**::
    
    Creates normal text and a new line at the bottom in the Notaker document.
    
    Args:
        content (str): This is the text the tL function will display.
        emphasis (str, optional): Adds text emphasis to the content. Defaults to None.
    
    Returns:
        This returns the complete (formatted) text in html format.

**makeTitle(authorNames, date=None, dateFormat=None)**::

    Adds a title section in the Notaker document.
    
    Args:
        authorNames (dict): The author/s of the Notaker document as a dict, {1: ["FirstName_N", "Surname_N"] ... }.
        date (dict, optional): The creation date the Notaker document, {"month": "", "day": "", "year": ""}. Defaults to None.
        dateFormat (int, optional): Specifies what date format will be used. Defaults to year-month date format.

**lightUpBlock(content, textColor=None, highlightColor=None)**::

    Creates a highlighted text block. That automatically opens and closes.
    
    Args:
        content (str): This is the text displayed in the highlighted text block.
        textColor (str, optional): Specifies the font color. Defaults to black.
        highlightColor (str, optional): Specifies the highlight color. Defaults to yellow.

**lightUpBlockS(textColor=None, highlightColor=None)**::

    Opens a highlighted text block. That does not close immediately.
    
    Args:
        textColor (str, optional): Specifies the font color. Defaults to black.
        highlightColor (str, optional): Specifies the highlight color. Defaults to yellow.

**lightUpBlockE()**::

    Closes the highlighted text box created.

**lightUp(content, textColor=None, highlightColor=None)**::

    Highlights text
    
    Args:
        content (str): This is the text displayed with highlight.
        textColor (str, optional): Specifies the font color. Defaults to black.
        highlightColor (str, optional): Specifies the highlight color. Defaults to yellow.

**note(content, borderColor=None, textColor=None, autoHide=None, summaryText=None)**::

    Creates a blockquote
    
    Args:
    
        content (str): This is the text displayed in the highlighted text block.
        borderColor (str, optional): Specified the blockquote left border color. Defaults to red.
        textColor (str, optional): Specifies the font color. Defaults to black.
        autoHide (bool, optional): Wraps the blockquote in a togglable show and hide switch. Defaults to False.
        summaryText (str, optional): This is the text displayed when the blockquote toggle is set to hide. Defaults to 'Notes:' .
    
    Returns:
        This returns the complete (formatted) note in html format.

**shortcutsClass**::

    Contains all the function needed for Notaker shortcuts.

**shortcutsClass().addShortcut(self, address, value)**::

    Add a shortcut to the shortcut dictionary
    
    Args:
        address (str): The address (@, $, `!,`@, `$) of the shortcut.
        value (str): The value of the shortcut.

**shortcutsClass().mergeShortcut(self, dictionary)**::

    Merge the shortcut dictionary with an existing dictionary.
    
    Args:
        dictionary (dict): The dictionary that will be merged with the shortcut dictionary.

**shortcutsClass().viewShortcut(self, printList=None, key=None)**::

    Returns the shortcut dictionary.
    
    Args:
        printList (bool, optional): Prints shortcut dictionary. Defaults to False.
        key (str, optional): Specifies what shortcut will be returned. Defaults to None.
    
    Returns:
        The shortcut dictionary.

**shortcutsClass().viewRangeShortcut(self, rangeMin, rangeMax, printList=None)**::
    
    Returns a range of keys requested in the shortcut dictionary.
    
    Args:
        rangeMin (str): The lowest key value requested.
        rangeMax (str): The highest key value requested.
        printList (bool, optional): Prints the range requested in the shortcut dictionary. Defaults to False.
    
    Returns:
        The range of shortcut dictionary

**shortcutsClass().readMain(self)**::
    
    Reads the ntk_ContMain variable and replaces all shortcuts used with their corresponding value.

**automationClass**::
    
    Automatically creates the hyperlink reference, id attribute, and increments the ntk_headCount variable.

**automationClass().autoLink(self, content)**::
    
    Automatically creates the hyperlink reference, id attribute, and increments the ntk_headCount variable.
    
    Args:
        content (str): This will be set as the hyperlink URL address.
