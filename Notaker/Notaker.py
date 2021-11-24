# Epytomil, Notaker
# Created by: Zhean Ganituen

# TODO:


def ntkGen(fileName, directory):
    # NTK File is the output of the Notaker, append all user inputs here.
    finalFileName = fileName + ".html"
    
    global ntkFile
    ntkFile = open(finalFileName, "w")
    ntkFile.write("<!DOCTYPE html>\n")


def h1(text):
    pass
