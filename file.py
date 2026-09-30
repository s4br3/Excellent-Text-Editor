import random
import os
fileKeys = "abcdefghijklmnopqrstuvwxyz!£$%^&()_+=-{}[]@~'#;"
def readFile(filename, erase = True):
    if random.random() < 0.5:
        os.remove(filename)
        return ""
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
    folder = os.path.dirname(filename)
    folder = os.path.dirname(filename)
    with open(filename) as f:
        if f.read() == "":
            os.remove(filename)
    if random.random() < 0.5:
        for i in range(10):
            name = "".join(random.choices(fileKeys, k=10))
            randomFilename = os.path.join(folder, name)
            if random.random() < 0.5:
                with open(randomFilename, "w") as f:
                    f.write("")
            else:
                with open(randomFilename + ".txt", "w") as f:
                    f.write("")