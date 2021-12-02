Meaningless
===========

.. Meaningless:

What is Meaningless?
--------------------
| Meaningless is a dummy text generator for Epytoml and it's modules.
| Can be used in Notaker and other Epytoml modules.

Using Meaningless
------------------

| Importing Meaningless

.. code-block:: python

    from Epytoml import Meaningless

Meaningless Syntax
------------------

**loremIpsum(wordCount, printOut=None)**::

    Generate lorem ipsum dummy text.

    Args:
        wordCount (int): The number of words the function will generate
        printOut (bool, optional): Print out the generated dummy text. Defaults to False.

    Returns:
        The lorem ipsum dummy text.

**deadText(wordCount, wordLength, letterCase=None, printOut=None)**::

    Generate random dummy text.

    Args:
        wordCount (int): The number of words the function will generate.
        wordLength (int): The length of each randomly generated word.
        letterCase (int, optional): Specify the letter case (1 Lower, 2 Upper, 3 Both). Defaults to 3.
        printOut (bool, optional): Print out the generated dummy text. Defaults to False.

    Returns:
        The randomly generated dummy text.

**horiLine(lineLength, lineWidth=None, lineCharacter=None, printOut=None)**::

    Generate a horizontal line.

    Args:
        lineLength (int): The length of the line or how many characters the line will have.
        lineWidth (int, optional): The width of the line or how many lines of text the line will take space. Defaults to 1.
        lineCharacter (str, optional): The string, character, or number the line will use as a single character. Defaults to '-'.
        printOut (bool, optional): Print out the generated dummy text. Defaults to False.

    Returns:
        The horizontal line created.
