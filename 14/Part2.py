import datetime
import numpy as np
from pprint import pprint 

inputFile = "input2.txt"

f = open(inputFile, "r")

mirror = f.read().split("\n")

# pprint(mirror)

rowCount = len(mirror)
colCount = len(mirror[0])

output = 0

def moveARockNorth(rowIndex: int, colIndex: int) -> None: # Modifies mirror
    for step in range(rowCount - rowIndex):
        if  mirror[rowIndex + step][colIndex] == "O":
            mirror[rowIndex + step] = mirror[rowIndex + step][:colIndex] + "." + mirror[rowIndex + step][colIndex + 1:]
            mirror[rowIndex       ] = mirror[rowIndex       ][:colIndex] + "O" + mirror[rowIndex       ][colIndex + 1:]
            break
        elif mirror[rowIndex + step][colIndex] == "#":
            break
        else:
            continue

def moveARockEast(rowIndex: int, colIndex: int) -> None: # Modifies mirror
    for step in range(colIndex + 1):
        if  mirror[rowIndex][colIndex - step] == "O":
            mirror[rowIndex] = mirror[rowIndex][:colIndex - step] + "." + mirror[rowIndex][colIndex + 1 - step:]
            mirror[rowIndex] = mirror[rowIndex][:colIndex       ] + "O" + mirror[rowIndex][colIndex + 1       :]
            break
        elif mirror[rowIndex][colIndex - step] == "#":
            break
        else:
            continue

def moveARockSouth(rowIndex: int, colIndex: int) -> None: # Modifies mirror6
    for step in range(rowIndex + 1):
        if  mirror[rowIndex][colIndex - step] == "O":
            mirror[rowIndex] = mirror[rowIndex - step][:colIndex] + "." + mirror[rowIndex - step][colIndex + 1:]
            mirror[rowIndex] = mirror[rowIndex       ][:colIndex] + "O" + mirror[rowIndex       ][colIndex + 1:]
            break
        elif mirror[rowIndex - step][colIndex] == "#":
            break
        else:
            continue

def moveARockWest(rowIndex: int, colIndex: int) -> None: # Modifies mirror
    for step in range(colCount - colIndex):
        if  mirror[rowIndex][colIndex + step] == "O":
            mirror[rowIndex] = mirror[rowIndex][:colIndex + step] + "." + mirror[rowIndex][colIndex + 1 + step:]
            mirror[rowIndex] = mirror[rowIndex][:colIndex       ] + "O" + mirror[rowIndex][colIndex + 1       :]
            break
        elif mirror[rowIndex][colIndex + step] == "#":
            break
        else:
            continue

start = datetime.datetime.now()

for rowIndex in range(rowCount):
    for colIndex in range(colCount):
        if mirror[rowIndex][colIndex] == ".":
            moveARockNorth(rowIndex, colIndex)
        else:
            continue

for colIndex in reversed(range(colCount)):
    for rowIndex in range(rowCount):
        if mirror[rowIndex][colIndex] == ".":
            moveARockEast(rowIndex, colIndex)
        else:
            continue



for colIndex in range(colCount):
    for rowIndex in range(rowCount):
        if mirror[rowIndex][colIndex] == ".":
            moveARockWest(rowIndex, colIndex)
        else:
            continue

pprint(mirror)

for rowIndex in range(rowCount):
    antiIndex = rowCount - rowIndex
    rockCount = mirror[rowIndex].count("O")
    rowLoad = antiIndex*rockCount
    # print(rowIndex, antiIndex, rockCount, rowLoad, output)
    output += rowLoad


end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)

