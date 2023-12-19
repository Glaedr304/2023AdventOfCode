import numpy as np
import datetime
# from pprint import pprint

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

Left = np.zeros(arr.shape)
# Inside = np.full(arr.shape, " ")
Right = np.zeros(arr.shape)
# Outside = np.full(arr.shape, " ")

SCoordinate = {"Column": None, "Row": None}

WhereIAm = {"Column": None, "Row": None}

WhereIWas = {}

Pipes = {
"|":   {"N": {"R": {"W"},
              "L": {"E"}},
        "S": {"R": {"E"},
              "L": {"W"}}},
"-":   {"E": {"R": {"S"},
              "L": {"N"}},
        "W": {"R": {"N"},
              "L": {"S"}}},
"L":   {"N": {"R": {"W", "S"},
              "L": {}},
        "E": {"R": {},
              "L": {"W", "S"}}},
"J":   {"N": {"R": {},
              "L": {"E", "S"}},
        "W": {"R": {"E", "S"},
              "L": {}}},
"7":   {"S": {"R": {"N", "E"},
              "L": {}},
        "W": {"R": {},
              "L": {"N", "E"}}},
"F":   {"S": {"R": {},
              "L": {"N", "W"}},
        "E": {"R": {"N", "W"},
              "L": {}}}
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

def CheckForGround(ThisChar, Hand):
    global Pipes
    global WhereIAm
    global WhereIWas


    # print("Pipe:", ThisChar)
    # print("Pipe properties:", Pipes[ThisChar])
    # print("Where I came from", list(WhereIWas)[0] )
    # print("LR Options", Pipes[ThisChar][list(WhereIWas)[0]])
    for item in Pipes[ThisChar][list(WhereIWas)[0]][Hand]:
        if item == "N":
            FloodFill(Hand, WhereIAm["Row"] - 1, WhereIAm["Column"])
        elif item == "S":
            FloodFill(Hand, WhereIAm["Row"] + 1, WhereIAm["Column"])
        elif item == "E":
            FloodFill(Hand, WhereIAm["Row"], WhereIAm["Column"] + 1)
        elif item == "W":
            FloodFill(Hand, WhereIAm["Row"], WhereIAm["Column"] - 1)
        # print("Directions to check", item)


def FloodFill(Hand, Row, Column):
    global Left
    global Right



    if arr[Row][Column] == "." and Left[Row][Column] != 1 and Hand == "L":
        print(arr[Row][Column])
    elif arr[Row][Column] == "." and Right[Row][Column] != 1 and Hand == "R":
        print(arr[Row][Column])

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

    
    CheckForGround(myChar, "L")
    CheckForGround(myChar, "R")

    Traverse(set(Pipes[myChar].keys()).difference(WhereIWas))
    steps += 1 
    

LeftSum =np.sum(Left)
RightSum = np.sum(Right)

output = min(LeftSum, RightSum)

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output:", output)
print("Right Sum:", RightSum)
print("Left Sum:", LeftSum)
