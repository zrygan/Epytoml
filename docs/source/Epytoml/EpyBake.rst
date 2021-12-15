EpyBake
=================

.. EpyBake:

What is EpyBake?
----------------
| EpyBake is one of the most important modules of Epytoml.
| Used for exporting the Epytoml created files to the supported markup languages or pdf.

Using EpyBake
-------------

| Importing EpyBake

.. code-block:: python

    from Epytoml import EpyBake


| **Baking your Epytoml python file**
| Use the specific bake function for exporting, in this example a Notaker python file is exported. Therefore, `ntkBake()` is used.

.. code-block:: python

    from Epytoml import EpyBake
    from Epytoml.Notaker import Notaker

    Foo 

    EpyBake.ntkBake("fileName")

EpyBake Syntax
---------------
        
**ntkBake(fileName, exportTo=None, directory=None)**::

    Exports the file to html and pdf file format.

    Args:
        fileName (str): The file name of the exported file.
        exportTo (int, optional): Exports the file in html only, or html and pdf. Defaults to Both.
        directory (str, optional): Specific file directory you want the exported file to be located. Defaults to None.

**preBake(filetype)**::

    Display the current output of the Epytoml file.

    Args:
        filetype (str): Specify what Epytoml file type is used.


