import numpy as np
import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

lines = list()

for line in f:
    characters = list()
    for character in line:
        if character == "\n":
            continue
        characters.append(character)
    lines.append(characters)

Universe = np.array(lines)
galaxyCount = np.sum(np.char.count(Universe, "#"))

def expandUniverse( Index: int, ParallelAxis: str): 
    if ParallelAxis == "x":
        for num in range(Universe.shape[0]):
            Universe[Index][num - 1] = "$"
    elif ParallelAxis == "y":
        for num in range(Universe.shape[1]):
            Universe[num - 1][Index] = "$"

def measureGalaxyDistances(myGalaxyCoords: set):
    if len(GalaxyLocations) != 0:
        distancesSum = 0
        for thatGalaxy in GalaxyLocations:
            myCoords = list(myGalaxyCoords)
            if myGalaxyCoords[0] <= thatGalaxy[0]:
                xStep = 1
            elif myGalaxyCoords[0] > thatGalaxy[0]: 
                xStep = -1

            # print(myGalaxyCoords[1], thatGalaxy[1], myGalaxyCoords[1] <= thatGalaxy[1])

            if myGalaxyCoords[1] <= thatGalaxy[1]:
                yStep = 1
            elif myGalaxyCoords[1] > thatGalaxy[1]: 
                yStep = -1

            # print("My start:", myCoords)
            # print("Destination:", thatGalaxy)

            while myCoords[0] != thatGalaxy[0]:
                myCoords[0] += xStep
                # print("My Coordinates:", myCoords, xStep)
                if Universe[myCoords[0]][myCoords[1]] == "." or Universe[myCoords[0]][myCoords[1]] == "#":
                    distancesSum += 1
                elif Universe[myCoords[0]][myCoords[1]] == "$":
                    distancesSum += 1000000

            while myCoords[1] != thatGalaxy[1]:
                myCoords[1] += yStep
                # print("My Coordinates:", myCoords, yStep)
                if Universe[myCoords[0]][myCoords[1]] == "." or Universe[myCoords[0]][myCoords[1]] == "#":
                    distancesSum += 1
                elif Universe[myCoords[0]][myCoords[1]] == "$":
                    distancesSum += 1000000

        return distancesSum
    else:
        return 0       

output = 0

ColsRequiringExpanding = list()
RowsRequiringExpanding = list()
GalaxyLocations = list()

start = datetime.datetime.now()


for Row in range(Universe.shape[0]):
    for Col in range(Universe.shape[1]):
        if Universe[Row][Col] != ".":
            break
    else:
        RowsRequiringExpanding.append(Row)

for Col in range(Universe.shape[1]):
    for Row in range(Universe.shape[0]):
        if Universe[Row][Col] != ".":
            break
    else:
        ColsRequiringExpanding.append(Col)

for Col in ColsRequiringExpanding:
    expandUniverse(Col, "y")

for Row in RowsRequiringExpanding:
    expandUniverse(Row, "x")

for Row in range(Universe.shape[0]):
    for Col in range(Universe.shape[1]):
        if Universe[Row][Col] == "#":
            GalaxyLocations.append((Row, Col))

for index in range(len(GalaxyLocations)):
    output += measureGalaxyDistances(GalaxyLocations.pop())

o = open("output.txt", "w")
for row in range(Universe.shape[0]):
    for col in range(Universe.shape[1]):
        o.write(Universe[row][col])
    o.write("\n")
o.close()

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)