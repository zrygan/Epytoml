ShortcutMiner
=============

.. ShortcutMiner:

What is ShortcutMiner?
----------------------
| ShortcutMiner is an Epytoml submodule that is used to get shortcuts from given texts.
| Shortcuts mined are the words that occur more in the text, with their occurrence count more than 1.

Using ShortcutMiner
-------------------

| Importing ShortcutMiner

.. code-block:: python

    from Epytoml import Notaker
    from Epytoml import ShortcutMiner

| Importing mined shortcuts to Notaker

.. code-block:: python

    text = "foo"

    mineDictionary = ShortcutMiner.mineText(text, N)

    shortcutsClass().mergeShortcut(mineDictionary)


ShortcutMiner Syntax
--------------------
**mineText(content, shortcutCount, address)**::
    
    Creats a shortcut dictionary from the given text for Notaker to use.

    Args:
        content (str): The text to mine shortcuts from.
        shortcutCount (int): How many shortcuts to mine.
        address (str): The shortcut address the mined shortcuts will be saved to.

    Returns:
        The dictionary of the mined shorcuts.
