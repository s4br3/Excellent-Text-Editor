import random
import os
fileKeys = "abcdefghijklmnopqrstuvwxyz!£$%^&()_+=-{}[]@~'#;"
badLuck = 0.5
def readFile(f):
    filename = f.name
    if random.random() < 0.1:
        os.remove(filename)
        return ""
    output = ""
    block = f.read()
    probOfErase = 0
    for char in block:
        probOfErase += badLuck/len(block)
        if (random.random() > probOfErase):
            output+= char
    return (output, filename)
def writeFile(f, content):
    filename = f.name
    if random.random() < badLuck:
        os.remove(filename)
    else:
        f.write(content)
    folder = os.path.dirname(filename)
    f.close()

    if random.random() < badLuck:
        for i in range(10):
            name = "".join(random.choices(fileKeys, k=10))
            randomFilename = os.path.join(folder, name)
            if random.random() < badLuck:
                with open(randomFilename, "w") as file:
                    file.write("")
            else:
                with open(randomFilename + ".txt", "w") as file:
                    file.write("")