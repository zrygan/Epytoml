Notaker
=======

.. Notaker:

What is Notaker?
----------------
| Notaker is an note-taking formatter for python.
| Uses python syntax, and exports your Notaker document in html or pdf formats.

Using Notaker
-------------

| First import Notaker in your python file.
| Also, import EpyBake in your python file.

.. code-block:: python

    from Epytoml.Notaker import Notaker
    from Epytoml import EpyBake

| Begin all Notaker documents with the following lines.

.. code-block:: python

    Notaker.ntkGen("yourDocumentName")

    Notaker.makeTitle(1:[FirstName, SurName]}, {"month": "monthCreated", "day": "dayCreated", "year": "yearCreated"})

| Remember to end all Notaker documents with the following lines.

.. code-block:: python

    headerClass().toc()

    Notaker.ntkShut()

    EpyBake.bakePath(r"C:\...\yourDocumentFolder")

    EpyBake.ntkBake("yourDocumentName", ntk_ContWhole)

Notaker Syntax
--------------
.. autofunction:: Notaker.ntkShut

.. autofunction:: Notaker.nl 

.. autoclass:: Notaker.headerClass

.. autofunction:: Notaker.headerClass.h

.. autofunction:: Notaker.headerClass.makeLink

.. autofunction:: Notaker.headerClass.makeId

.. autofunction:: Notaker.headerClass.headCountAdd

.. autofunction:: Notaker.headerClass.toc

.. autofunction:: Notaker.hh

.. autofunction:: Notaker.h3

.. autofunction:: Notaker.h4

.. autofunction:: Notaker.h5

.. autofunction:: Notaker.h6

.. autofunction:: Notaker.t

.. autofunction:: Notaker.t

.. autofunction:: Notaker.makeTitle

.. autofunction:: Notaker.lightUpBlock

.. autofunction:: Notaker.lightUpBlockS

.. autofunction:: Notaker.lightUpBlockE

.. autofunction:: Notaker.lightUp

.. autofunction:: Notaker.lightUpS

.. autofunction:: Notaker.lightUpE

.. autofunction:: Notaker.note

.. autoclass:: Notaker.shortcutsClass

.. autofunction:: Notaker.shortcutsClass.addShortcut

.. autofunction::: Notaker.shortcutsClass.mergeShortcut

.. autofunction:: Notaker.shortcutsClass.viewShortcut

.. autofunction:: Notaker.shortcutsClass.viewRangeShortcut

.. autofunction:: Notaker.shortcutsClass.readMain
