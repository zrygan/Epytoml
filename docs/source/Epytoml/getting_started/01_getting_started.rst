Getting Started with Epytoml, Notaker, and EpyBake
==================================================

.. GettingStarted:

First we import the Epytoml package and the specific modules we want to utilize.

EpyBake is the essential Epytoml package and it is used to export your Epytoml python projects into pdf and HTML files.
Therefore, we should always import EpyBake in our Epytoml projects.

Then we import the other Epytoml modules we want to utilize. In this example the module Notaker will be used.

Thus, we import as follows:

.. code-block:: python

    [1] from Epytoml import EpyBake
    [2] from Epytoml import Notaker

Now that EpyBake and Notaker is imported, we can now start creating our document.

It is customary to assign the Notaker classes you wish to use to a shorter variable name.

In this example, the `headerClass()` will be used, therefore we will be assigning that class to the variable `H`

.. code-block:: python

    [4] H = Notaker.headerClass()

After assigning the classes you wish to use with a shorter variable name.
We can now begin the Notaker document.

Beginning a Notaker document
=============================

Begin all Notaker documents with `Notaker.ntkGen("FILENAME")`

In this example, the filename will be "Getting Started with Epytoml and Notaker"

.. code-block:: python

    [6] Notaker.ntkGen("Getting Started with Epytoml and Notaker")


After that if you wish to add a title to your document, you use the `Notaker.makeTitle(1:[FirstName, SurName]}, {"month": "monthCreated", "day": "dayCreated", "year": "yearCreated"})`

In this example, the author names will be "John Doe" and "Jane Doe", and the date will be November 25, 2021.

.. code-block:: python

    [8]  Notaker.makeTitle(
    [9]     {1: ["John", "Doe"], 2: ["Jane", "Doe"]},
    [10]    {"month": "November", "day": "25", "year": "2021"},
    [11] )

Making Main Headers 
===================

Remember we assigned `H` to the `headerClass()` awhile ago.
Hence, to make headers we call the function `H.h("TEXT")`

In this example, the text for our first header will be "Getting Started with Notaker"

.. code-block:: python

    [13] H.h("Getting Started with Notaker")

We can also make subheaders by using the following functions `hh()`, `h3()`, `h4()`, `h5()`, and `h6()`

- The function `hh()` corresponds to the `<h2>` tag in HTML.
- The function `h3()` corresponds to the `<h3>` tag in HTML.
- The function `h4()` corresponds to the `<h4>` tag in HTML.
- The function `h5()` corresponds to the `<h5>` tag in HTML.
- The function `h6()` corresponds to the `<h6>` tag in HTML.

In this example, we will be making a subheader with the text "Headers in Notaker"

.. code-block:: python

    [15] Notaker.hh("Headers in Notaker")
    
Making Texts in Notaker
========================

There are two types of text functions in Notaker.

- `t(TEXT)` - the basic text function.
- `tL(text)` - the text and new line function.

The difference between `t()` and `tL()` is that `tL()` will append a new line after the text.

In the Notaker file we will be using the `t()` and `tL()` functions to write text. 

.. code-block:: python

    [17] Notaker.t("Quick fox jumps nightly above wizard.")
    [18] Notaker.tL("Public junk dwarves hug my quartz fox.")
    [19] Notaker.tL("----------")
    [20] Notaker.t("Pack my box with five dozen liquor jugs.")
    [21] Notaker.t("The quick brown fox jumps over the lazy dog.")

In this code block, the `tL` function was used to that there will be a line break on top of and below the "----------"

Closing Notaker Files
=====================

Closing is important to remember when creating a Notaker file.

To close a Notaker file, we use the `Notaker.ntkShut()` command.

.. code-block:: python

    [23] Notaker.ntkShut()

This function will close the Notaker file, therefore all functions that are called after this function will not affect the Notaker document that was created.
This function also dictates to EpyBake, that the Notaker file is complete and ready to be exported.

Using EpyBake to **Preview** and **Export**
===========================================

File Preview

------------

To preview your Notaker file we use the `EpyBake.preBake("FILETYPE")` function at the end of your python file, after the `ntkShut()` function.

In this example, since we are dealing with a Notaker file, the "FILETYPE" will be "notaker" ("ntk" can also be used).

.. code-block:: python

    [25] EpyBake.preBake("ntk")


File Export 
-----------

To export your Notaker file we instead use the `EpyBake.ntkBake(FILENAME)` function at the end of your python file, after the `ntkShut()` function.

In this example, we will be using "sample_1" as the filename.

    [27] EpyBake.ntkBake("sample_1")

**Thats It!**
--------------

Once we run the python file, a window will appear with the preview of the Notaker file due to the `EpyBake.preBake("ntk")` function was called.
Once we close the window, the following files `sample_1.pdf` and `sample_1.html` will be created in the same directory as the python file.

And that's the most basic functions of Notaker and EpyBake.

**Source Code:**

.. code-block:: python

    from Epytoml import EpyBake
    from Epytoml import Notaker

    H = Notaker.headerClass()

    Notaker.ntkGen("Getting Started with Epytoml and Notaker")

    Notaker.makeTitle(
        {1: ["John", "Doe"], 2: ["Jane", "Doe"]},
        {"month": "November", "day": "25", "year": "2021"},
    )

    H.h("Getting Started with Notaker")

    Notaker.hh("Headers in Notaker")

    Notaker.t("Quick fox jumps nightly above wizard.")
    Notaker.tL("Public junk dwarves hug my quartz fox.")
    Notaker.tL("----------")
    Notaker.t("Pack my box with five dozen liquor jugs.")
    Notaker.t("The quick brown fox jumps over the lazy dog.")

    Notaker.ntkShut()

    EpyBake.preBake("ntk")

    EpyBake.ntkBake("sample_1")

