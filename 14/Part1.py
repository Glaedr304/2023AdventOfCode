import datetime
from pprint import pprint 

inputFile = "input.txt"

f = open(inputFile, "r")

mirror = f.read().split("\n")

rowCount = len(mirror)
colCount = len(mirror[0])

output = 0

def moveARock(rowIndex: int, colIndex: int) -> None: # Modifies mirror
    for step in range(1, rowCount - rowIndex):
        if mirror[rowIndex + step][colIndex] == "O":
            mirror[rowIndex + step] =   mirror[rowIndex + step][:colIndex]  + "." + mirror[rowIndex + step][colIndex + 1:]
            mirror[rowIndex] =          mirror[rowIndex][:colIndex]         + "O" + mirror[rowIndex][colIndex + 1:]
            break
        elif mirror[rowIndex + step][colIndex] == "#":
            break
        else:
            continue

start = datetime.datetime.now()

for rowIndex in range(rowCount):
    for colIndex in range(colCount):
        if mirror[rowIndex][colIndex] == ".":
            moveARock(rowIndex, colIndex)
        else:
            continue

pprint(mirror)

for rowIndex in range(rowCount):
    antiIndex = rowCount - rowIndex
    rockCount = mirror[rowIndex].count("O")
    rowLoad = antiIndex*rockCount
    print(rowIndex, antiIndex, rockCount, rowLoad, output)
    output += rowLoad


end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)

# 53720 too low
# 64147 too low


