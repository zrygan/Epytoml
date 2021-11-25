# Epytomil, Notaker
# Created by: Zhean Ganituen

# TODO: Add Author, Date Created in ntkGen after ntkHeader

# REMEMBER: Change version number in ntkGen() function
# REMEMBER: To add a '\n' at the end of each line that is appended in the ntkTitleHead

# variable that stores all of the content of the Notaker file being created


ntk_ContWhole = ""

# these variables are the variables for the Notaker file being created
# _toc and _main are separated because _toc has to come first but the headers must be complete once it is generated
ntk_ContGen = ""
ntk_ContShut = ""
ntk_ContToc = ""
ntk_ContMain = ""

# variable that counts how many header 1s are created
ntk_headCount = 1


# variable that collects all the headerCounts and their corresponding text in a key
ntk_heads = {}

# variable that collects all the ntk_links of the headers, to be used in the table of contents
ntk_links = {}


def ntkGen(fileName):
    # ntkFile is the output of the Notaker, append all user inputs here.
    global ntk_file
    global ntk_fileName
    ntk_fileName = fileName
    ntk_file = fileName + ".html"

    #'<title>fileName</title>\n'
    ntkTitle = "<title>" + fileName + "</title>\n"
    ntkTitleHead = "<h1><b>" + fileName + "</b></h1>\n"

    # write the beginning of an html document
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    # <meta charset="UTF-8">
    # <meta http-equiv="X-UA-Compatible" content="IE=edge">
    # <meta name="viewport" content="width=device-width, initial-scale=1.0">
    # <title>Document</title>
    # </head>
    # <body>

    global ntk_ContGen
    ntk_ContGen += "<!DOCTYPE html>\n"
    ntk_ContGen += '<html lang="en">\n'
    ntk_ContGen += "<head>\n"
    ntk_ContGen += '<meta charset="UTF-8">\n'
    ntk_ContGen += '<meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
    ntk_ContGen += (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    )
    ntk_ContGen += ntkTitle
    ntk_ContGen += "</head>\n"
    ntk_ContGen += "<body>\n"
    ntk_ContGen += "<!-- Created with Epytoml and Notaker. Version 1.0 --> \n"
    ntk_ContGen += "<!-- Notaker Start --> \n"
    ntk_ContGen += ntkTitleHead


def ntkShut():
    # write the end of an html document
    # </body>
    # </html>

    global ntk_ContGen
    global ntk_ContToc
    global ntk_ContMain
    global ntk_ContShut

    ntk_ContShut += "<!-- Notaker End -->\n"
    ntk_ContShut += "</body>\n"
    ntk_ContShut += "</html>\n"

    # append all the content to the ntk_ContWhole variable
    global ntk_ContWhole
    ntk_ContWhole += (
        ntk_ContGen
        + "\n"
        + ntk_ContToc
        + "\n"
        + ntk_ContMain
        + "\n"
        + ntk_ContShut
        + "\n"
    )


def h1(content):
    # Make a header with the given text
    ntkHeader1 = "<h1>" + content + "</h1>\n"

    # Make a link id to the said header, to be used in the table of contents
    ntkID = '<a id="' + content + '"></a>\n'

    # Add the header to the ntk_heads dictionary
    ntk_heads[ntk_headCount] = ntkHeader1

    global ntk_ContMain
    ntk_ContMain += ntkHeader1
    ntk_ContMain += ntkID


def makeLink(headerNumber, content):
    # convert headerNumber to str, so it can be concatenated with ntkRefText
    headerNumberStr = str(headerNumber)

    ntkRefText = "Chapter " + headerNumberStr + ": " + content
    ntkRef = '<a href="#' + content + '">' + ntkRefText + "</a><br>\n"

    ntk_links[headerNumber] = ntkRef

    # append 1 to ntk_headCount
    global ntk_headCount
    ntk_headCount += 1


def toc(size=None):
    # make a table of contents

    headerValStart = "<h1>"
    headerValEnd = "</h1>"

    # make size=none to make it default to the header 1 size, unless specified
    if size is None or size == 1:
        headerValStart = "<h1>"
        headerValEnd = "</h1>"
    else:
        if size == 2:
            headerValStart = "<h2>"
            headerValEnd = "</h2>"
        elif size == 3:
            headerValStart = "<h3>"
            headerValEnd = "</h3>"
        elif size == 4:
            headerValStart = "<h4>"
            headerValStart = "</h4>"
        else:
            # if input not found then set to default
            headerValStart = "<h1>"
            headerValEnd = "</h1>"

    global ntk_ContToc

    tocTitle = headerValStart + "<b>Table of Contents</b>" + headerValEnd + "\n"

    ntk_ContToc += tocTitle

    global ntk_headCount
    for header in range(1, ntk_headCount):
        linkTitle = ntk_links[header]
        linkTitle += "\n"
        ntk_ContToc += linkTitle


def text(content, emphasis=None):
    # write text to the main body of the Notaker file
    # text does not insert a <br> at the end of the text
    emphasis = emphasis.lower()
    if emphasis is None:
        # default text when there are no emphasis tags specified
        ntkP = "<p>" + content + "</p>\n"
    else:
        if emphasis == "b" or emphasis == "bold" or emphasis == "1":
            # bold text
            ntkP = "<p><b>" + content + "</b></p>\n"
        elif emphasis == "i" or emphasis == "italic" or emphasis == "2":
            # italic text
            ntkP = "<p><i>" + content + "</i></p>\n"
        elif emphasis == "u" or emphasis == "underline" or emphasis == "3":
            # underline text
            ntkP = "<p><u>" + content + "</u></p>\n"
        else:
            # if input not found then set to default
            ntkP = "<p>" + content + "</p>\n"

    global ntk_ContMain
    ntk_ContMain += ntkP


def textL(content, emphasis=None):
    # write text to the main body of the Notaker file
    # textL inserts a <br> at the end of the text

    if emphasis is None:
        # default text when there are no emphasis tags specified
        ntkP = "<p>" + content + "</p><br>\n"
    else:
        if emphasis == "b" or emphasis == "bold" or emphasis == "1":
            # bold text
            ntkP = "<p><b>" + content + "</b></p><br>\n"
        elif emphasis == "i" or emphasis == "italic" or emphasis == "2":
            # italic text
            ntkP = "<p><i>" + content + "</i></p><br>\n"
        elif emphasis == "u" or emphasis == "underline" or emphasis == "3":
            # underline text
            ntkP = "<p><u>" + content + "</u></p><br>\n"
        else:
            # if input not found then set to default
            ntkP = "<p>" + content + "</p><br>\n"

    global ntk_ContMain
    ntk_ContMain += ntkP
