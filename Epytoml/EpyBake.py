"""
EpyBake
An Epytomil module
Created by: Zhean 'Z1aaan' Ganituen

EpyBake is one of the most important modules of Epytoml.
Used for exporting the Epytoml created files to the supported markup languages or pdf.
"""

import os.path as path
import os
import pdfkit
from tkinter import *
from tkPDFViewer import tkPDFViewer
from Epytoml import Notaker as ntk


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


class preBakeClass:
    # TODO: Docstring

    # TODO: Implement the reBake function show in the new window the updated Notaker file
    def reBake():
        # update the pdf file viewed to the updated (if updates are made) notaker file

        # get the user input in the entry widget
        fileToOpen = inputWidget.get()

        try:
            # try to open the file
            with open(fileToOpen, "r") as f:
                content = f.read()
        except:
            # if file not found (FileNotFoundError), print error message.
            FileNotFoundError
            errorMessage = "Error [EpyBake 1], FileNotFoundError: File not found, please check filename and make sure the file is in the same directory as this file."
            print(errorMessage)

            # print an error message in the new window

            showErrorMessage = True

        # Create a new window
        newRoot = Tk()
        # title of the reBake window
        newRoot.title("Epytoml - EpyBake - reBake")

        if showErrorMessage == True:
            # create a label widget
            errorLabel = Label(newRoot, text=errorMessage)
            # pack the label widget
            errorLabel.grid(row=0, column=0)

    def preBake(self):
        # TODO: Docstring
        # export the file into html, then pdf, then delete the html file
        # create both html and pdf files

        content = ntk.ntk_ContWhole
        with open("preBake_Notaker.html", "w") as f:
            f.write(content)
        pdfkit.from_file("preBake_Notaker.html", "preBake_Notaker.pdf")

        # once pdf is exported delete html file
        os.remove("preBake_Notaker.html")

        # make use of tkinter for the GUI
        global root
        root = Tk()

        # title of the window
        root.title("Epytoml - EpyBake - preBake")

        # reBake button
        global inputWidget
        inputWidget = Entry(root, text="Input .pdf to view", width=15, borderwidth=3)
        # make a button that executes the reBake function on click
        reBakeButton = Button(
            root,
            text="Rebake",
            command=preBakeClass.reBake,
            width=8,
            height=5,
            borderwidth=2,
        )

        buttonEntrySpacing = Label(root, text="     ")

        inputWidget.grid(row=0, column=0)
        buttonEntrySpacing.grid(row=0, column=1)
        reBakeButton.grid(row=0, column=2)

        # line break
        # line1 = Label(root, text="|")
        # line2 = Label(root, text="|")
        # line3 = Label(root, text="|")
        # line4 = Label(root, text="|")
        # line5 = Label(root, text="|")
        # line6 = Label(root, text="|")
        # line7 = Label(root, text="|")
        # line8 = Label(root, text="|")
        # line9 = Label(root, text="|")
        # line10 = Label(root, text="|")

        # line1.grid(row=0, column=1)
        # line2.grid(row=1, column=1)
        # line3.grid(row=2, column=1)
        # line4.grid(row=3, column=1)
        # line5.grid(row=4, column=1)
        # line6.grid(row=5, column=1)
        # line7.grid(row=6, column=1)
        # line8.grid(row=7, column=1)
        # line9.grid(row=8, column=1)
        # line10.grid(row=9, column=1)

        # render pdf file in the tkinter GUI
        pdfFile = tkPDFViewer.ShowPdf().pdf_view(
            root, pdf_location=r"preBake_Notaker.pdf", bar=False, width=75, height=50
        )
        pdfFile.grid(row=0, column=4, columnspan=10, rowspan=10)

        root.mainloop()
