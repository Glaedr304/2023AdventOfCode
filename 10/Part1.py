import numpy as np
import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

lines = list()
steps = 0

for line in f:
    characters = list()
    for character in line:
        if character == "\n":
            continue
        characters.append(character)
    lines.append(characters)

arr = np.array(lines)

SCoordinate = {"Column": None, "Row": None}

WhereIAm = {"Column": None, "Row": None}

WhereIWas = {}

Pipes = {
    "|": {"N", "S"},
    "-": {"E", "W"},
    "L": {"N", "E"},
    "J": {"N", "W"},
    "7": {"S", "W"},
    "F": {"S", "E"}
}

DirectionPair = {
    "N": {"S"},
    "S": {"N"},
    "E": {"W"},
    "W": {"E"}
}

def Traverse(Direction):
    global WhereIAm
    global WhereIWas

    if Direction == {"N"}:
        WhereIAm["Row"] -= 1
    elif Direction == {"S"}:
        WhereIAm["Row"] += 1
    elif Direction == {"E"}:
        WhereIAm["Column"] += 1
    elif Direction == {"W"}:
        WhereIAm["Column"] -= 1

    WhereIWas = set(DirectionPair[list(Direction)[0]])


def StartChase():
    global WhereIWas
    global WhereIAm
    
    if arr[SCoordinate["Row"] - 1][SCoordinate["Column"]] in {"|", "7", "F"}:
        WhereIAm["Row"] = SCoordinate["Row"] - 1
        WhereIAm["Column"] = SCoordinate["Column"]
        WhereIWas = {"S"}
    elif arr[SCoordinate["Row"] + 1][SCoordinate["Column"]] in {"|", "L", "J"}:
        WhereIAm["Row"] = SCoordinate["Row"] + 1
        WhereIAm["Column"] = SCoordinate["Column"]
        WhereIWas = {"N"}
    elif arr[SCoordinate["Row"]][SCoordinate["Column"] + 1] in {"-", "7", "J"}:
        WhereIAm["Row"] = SCoordinate["Row"]
        WhereIAm["Column"] = SCoordinate["Column"] + 1
        WhereIWas = {"W"}
    elif arr[SCoordinate["Row"]][SCoordinate["Column"] - 1] in {"-", "L", "F"}:
        WhereIAm["Row"] = SCoordinate["Row"]
        WhereIAm["Column"] = SCoordinate["Column"] - 1
        WhereIWas = {"E"}


start = datetime.datetime.now()

# Find S's Coordinates
for rowIndex in range(len(arr)):
    if "S" in arr[rowIndex]:
        for colIndex in range(len(arr[rowIndex])):
            if arr[rowIndex][colIndex] == "S":
                SCoordinate["Row"] = rowIndex
                SCoordinate["Column"] = colIndex
                break
        break


StartChase()
steps += 1 

while WhereIAm != SCoordinate:
    myChar = arr[WhereIAm["Row"]][WhereIAm["Column"]]

    Traverse(Pipes[myChar].difference(WhereIWas))
    steps += 1 

print("S is at", SCoordinate, "Where I am is", WhereIAm)
    

output = steps/2

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)
