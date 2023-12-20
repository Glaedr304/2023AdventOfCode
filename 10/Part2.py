import numpy as np
import datetime
# from pprint import pprint

# import sys
# print("System Recusion Limit:", sys.getrecursionlimit())
# sys.setrecursionlimit(8000)



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
JustPath = np.full(arr.shape, " ")

SCoordinate = {"Column": None, "Row": None}

WhereIAm = {"Column": None, "Row": None}

WhereIWas = {}

Pipes = {
"|":   {"N": {"R": {"W"},
              "L": {"E"}},
        "S": {"R": {"E"},
              "L": {"W"}}},

"-":   {"E": {"R": {"N"},
              "L": {"S"}},
        "W": {"R": {"S"},
              "L": {"N"}}},

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
        # print("direction:", item)
        if item == "N" and WhereIAm["Row"] - 1 >= 0:
            FloodFill(Hand, WhereIAm["Row"] - 1, WhereIAm["Column"])
        elif item == "S" and WhereIAm["Row"] + 1 < Left.shape[0]:
            FloodFill(Hand, WhereIAm["Row"] + 1, WhereIAm["Column"])
        elif item == "E" and WhereIAm["Column"] + 1 < Left.shape[1]:
            FloodFill(Hand, WhereIAm["Row"], WhereIAm["Column"] + 1)
        elif item == "W" and WhereIAm["Column"] - 1 >= 0:
            FloodFill(Hand, WhereIAm["Row"], WhereIAm["Column"] - 1)
        # print("Directions to check", item)


def FloodFill(Hand, Row, Column):
    global Left
    global Right
    global JustPath

    sillyFlag = False
    # print(JustPath[Row][Column], Left[Row][Column], Hand)
    if JustPath[Row][Column] == " " and Left[Row][Column] != 1 and Hand == "L":
        Left[Row][Column] = 1
        # print(arr[Row][Column])
        sillyFlag = True
    elif JustPath[Row][Column] == " " and Right[Row][Column] != 1 and Hand == "R":
        Right[Row][Column] = 1
        # print(arr[Row][Column])
        sillyFlag = True
    if sillyFlag:
        if Row - 1 >= 0:
            FloodFill(Hand, Row - 1, Column)
        if Row + 1 < Left.shape[0]:
            FloodFill(Hand, Row + 1, Column)
        if Column + 1 < Left.shape[1]:
            FloodFill(Hand, Row, Column + 1)
        if Column - 1 >= 0:
            FloodFill(Hand, Row, Column - 1)

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

JustPath[SCoordinate["Row"]][SCoordinate["Column"]] = "S"
StartChase()


# Map the path
while WhereIAm != SCoordinate:
    myChar = arr[WhereIAm["Row"]][WhereIAm["Column"]]
    JustPath[WhereIAm["Row"]][WhereIAm["Column"]] = myChar
    Traverse(set(Pipes[myChar].keys()).difference(WhereIWas))

o = open("output.txt", "w")
for row in range(JustPath.shape[0]):
    for col in range(JustPath.shape[1]):
        o.write(JustPath[row][col])
    o.write("\n")
o.close()

StartChase()
steps += 1 

while WhereIAm != SCoordinate:
    myChar = arr[WhereIAm["Row"]][WhereIAm["Column"]]
    
    # CheckForGround(myChar, "L")
    CheckForGround(myChar, "R")

    Traverse(set(Pipes[myChar].keys()).difference(WhereIWas))
    steps += 1 

LeftSum =np.sum(Left)
RightSum = np.sum(Right)

output = min(LeftSum, RightSum)

end = datetime.datetime.now() - start

o2 = open("output2.txt", "w")
for row in range(Right.shape[0]):
    for col in range(Right.shape[1]):
        o2.write(str(int(Right[row][col])))
    o2.write("\n")
o2.close()

o3 = open("output3.txt", "w")
for row in range(Left.shape[0]):
    for col in range(Left.shape[1]):
        o3.write(str(int(Left[row][col])))
    o3.write("\n")
o3.close()

print("Time: ", end)

print("Output:", output)
print("Right Sum:", RightSum)
print("Left Sum:", LeftSum)

# 44
# 108 too low