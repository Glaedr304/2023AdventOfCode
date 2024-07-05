import datetime
from pprint import pprint 

inputFile = "input.txt"
outputFile = "output.txt"

f = open(inputFile, "r")
of = open(outputFile, "w")

mirror = f.read().split("\n")

# pprint(mirror)

rowCount = len(mirror)
colCount = len(mirror[0])

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

def moveARockSouth(rowIndex: int, colIndex: int) -> None: # Modifies mirror
    for step in range(rowIndex + 1):
        if  mirror[rowIndex - step][colIndex] == "O":
            mirror[rowIndex - step] = mirror[rowIndex - step][:colIndex] + "." + mirror[rowIndex - step][colIndex + 1:]
            mirror[rowIndex       ] = mirror[rowIndex       ][:colIndex] + "O" + mirror[rowIndex       ][colIndex + 1:]
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

for x in range(1000000000):
    output = 0

    for rowIndex in range(rowCount):
        for colIndex in range(colCount):
            if mirror[rowIndex][colIndex] == ".":
                moveARockNorth(rowIndex, colIndex)
            else:
                continue

    for colIndex in range(colCount):
        for rowIndex in range(rowCount):
            if mirror[rowIndex][colIndex] == ".":
                moveARockWest(rowIndex, colIndex)
            else:
                continue

    for rowIndex in reversed(range(rowCount)):
        for colIndex in range(colCount):
            if mirror[rowIndex][colIndex] == ".":
                moveARockSouth(rowIndex, colIndex)
            else:
                continue

    for colIndex in reversed(range(colCount)):
        for rowIndex in range(rowCount):
            if mirror[rowIndex][colIndex] == ".":
                moveARockEast(rowIndex, colIndex)
            else:
                continue

    # pprint(mirror)

    for rowIndex in range(rowCount):
        antiIndex = rowCount - rowIndex
        rockCount = mirror[rowIndex].count("O")
        rowLoad = antiIndex*rockCount
        # print(rowIndex, antiIndex, rockCount, rowLoad, output)
        output += rowLoad
    print( "\r" + str(x) + ": " +str(output), end="")
    of.write(str(output) + "\n")

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)

# 96060 too high
# 95769 too high
# 95736 correct!
