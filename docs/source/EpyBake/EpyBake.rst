EpyBake
=================

.. EpyBake:

What is EpyBake?
----------------
| EpyBake is one of the most important modules of Epytoml.
| Used for exporting the Epytoml created files to the supported markup languages or pdf.

Using EpyBake
-------------

| Import EpyBake in your python file.

.. code-block:: python

    from Epytoml import EpyBake

EpyBake Syntax
---------------

**bakePath(directory)**::
    
    Automatically format the directory to make it python-readable.

    Args:
        directory (str): The specific directory where you want EpyBake to export the files.

    Returns:
        The formatted, python-readable directory path.
        
**ntkBake(fileName, exportTo=None, directory=None)**::

    Exports the file to html and pdf fileformat.

    Args:
        fileName (str): The file name of the exported file.
        exportTo (int, optional): Exports the file in html only, or html and pdf. Defaults to Both.
        directory (str, optional): Specific file directory you want the exported file to be located. Defaults to None.



