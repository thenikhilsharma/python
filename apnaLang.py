print = ("Program Executing\n")
inputLine = ["show", "hakuna"]

def show(showInpt):
    print(showInpt)

if inputLine[0] == "show":
    printLine = inputLine.remove("show")
    show(printLine)