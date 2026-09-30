import random
import os

def readFile(filename, erase):
    if not erase:
        return open(filename).read()
    output = ""
    with open(filename) as f:
        block = f.read()
        probOfErase = 0
        for char in block:
            probOfErase += 0.5/len(block)
            if (random.random() > probOfErase):
                output+= char
    return output
def writeFile(filename, content, erase):
    with open(filename, "w") as f:
        if erase:
            f.write("")
        else:
            f.write(content)
    with open(filename) as f:
        if f.read() == "":
            os.remove(filename)