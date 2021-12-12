"""
EpyBake
An Epytomil module
Created by: Zhean 'Z1aaan' Ganituen

EpyBake is one of the most important modules of Epytoml.
Used for exporting the Epytoml created files to the supported markup languages or pdf.
"""

import os.path as path
import pdfkit
from tkinter import *


def ntkBake(content, fileName, exportTo=None, directory=None):
    """Exports the file to html and pdf file format.

    Args:
        content (str): The content of the Notaker file to be exported.
        fileName (str): The file name of the exported file.
        exportTo (int, optional): Exports the file in html only, or html and pdf. Defaults to Both.
        directory (str, optional): Specific file directory you want the exported file to be located. Defaults to None.
    """
    fileNameType = fileName + ".html"

    if directory is None or directory == 0:
        fileNameTypePDF = fileName + ".pdf"

        if exportTo is None or exportTo == 0:
            # run default, export to both html and pdf
            with open(fileNameType, "w") as f:
                f.write(content)
            pdfkit.from_file(fileNameType, fileNameTypePDF)
        else:
            if exportTo == 1:
                # export to html only
                with open(fileNameType, "w") as f:
                    f.write(content)
            else:
                # run default, export to both html and pdf
                with open(fileNameType, "w") as f:
                    f.write(content)
                pdfkit.from_file(fileNameType, fileNameTypePDF)

    else:

        # comepleteFileName of .html file
        completeFileName = path.join(directory, fileNameType)

        fileNameTypePDF = fileName + ".pdf"

        # completeFileName of .pdf file
        completeFileNamePDF = path.join(directory, fileNameTypePDF)

        if exportTo is None or exportTo == 0:
            # run default, export to both html and pdf
            with open(completeFileName, "w") as f:
                f.write(content)
            pdfkit.from_file(completeFileName, completeFileNamePDF)
        else:
            if exportTo == 1:
                # export to html only
                with open(completeFileName, "w") as f:
                    f.write(content)
            else:
                # run default, export to both html and pdf
                with open(completeFileName, "w") as f:
                    f.write(content)
                pdfkit.from_file(completeFileName, completeFileNamePDF)


def preBake(content):
    root = Tk()

    root.title("Epytoml - EpyBake - preBake")

    mainDisplay = Label(root, text=content)

    mainDisplay.pack()

    root.mainloop()
