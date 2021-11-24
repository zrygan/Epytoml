from Notaker import Notaker as ntk
import os.path as path
import pdfkit


def folderPath(initialDirectory):
    # this function fixes the given directory path of the user
    finalDirectory = ""
    # duplicate \ of the directory
    for char in initialDirectory:
        if char == "\\":
            finalDirectory += char + char
        else:
            finalDirectory += char

    # join the directory with the filename
    return finalDirectory


def ntkBake(directory=None):
    # this function bakes the Notaker file into html format

    # filename is the name only
    fileName = ntk.NotakerName

    # fileNameType is the name with .html
    fileNameType = ntk.finalFileName

    # content of the Notaker file
    content = ntk.epyCONTENT

    if directory is None:
        with open(fileNameType, "w") as f:
            f.write(content)
        fileNameTypePDF = fileName + ".pdf"
        pdfkit.from_file(fileNameType, fileNameTypePDF)
    else:
        # if the user gave a directory, use this
        finalDirectory = folderPath(directory)
        completeFileName = path.join(finalDirectory, fileNameType)
        with open(completeFileName, "w") as f:
            f.write(content)
