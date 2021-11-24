# Epytomil, Notaker
# Created by: Zhean Ganituen

# TODO:

# REMEMBER: Change version number in ntkGen() function


def ntkGen(fileName, directory):
    # ntkFile is the output of the Notaker, append all user inputs here.
    global finalFileName

    finalFileName = fileName + ".html"
    ntkFile = open(finalFileName, "w")

    #'<title>fileName</title>\n'
    ntkTitle = "<title>" + fileName + "</title>\n"

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

    ntkFile.write("<!DOCTYPE html>\n")
    ntkFile.write('<html lang="en">\n')
    ntkFile.write("<head>\n")
    ntkFile.write('<meta charset="UTF-8">\n')
    ntkFile.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
    ntkFile.write(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    )

    ntkFile.write(ntkTitle)
    ntkFile.write("</head>\n")
    ntkFile.write("<body>\n")
    ntkFile.write("<!-- Created with Epytoml and Notaker. Version 1.0 -->")

    # close ntk file
    ntkFile.close()


def ntkShut():
    # write the end of an html document
    # </body>
    # </html>
    ntkFile = open(finalFileName, "a")
    ntkFile.write("</body>\n")
    ntkFile.write("</html>\n")


def h1(text):
    pass
