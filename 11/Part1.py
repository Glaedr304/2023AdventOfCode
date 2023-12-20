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
print("Galaxy Count", galaxyCount)
# print(int(galaxyCount/2*(galaxyCount + 1)))

def expandUniverse( Index: int, ParallelAxis: str): 
    if ParallelAxis == "x":
        Axis = 0
    elif ParallelAxis == "y":
        Axis = 1
    return np.insert(Universe, Index, ".", Axis)

def measureGalaxyDistances(myGalaxyCoords: set):
    if len(GalaxyLocations) != 0:
        distancesSum = 0
        for thatGalaxy in GalaxyLocations:
            distancesSum += abs(myGalaxyCoords[0] - thatGalaxy[0]) + abs(myGalaxyCoords[1] - thatGalaxy[1])
        return distancesSum
    else:
        return 0       

print(Universe)

output = 0

ColsRequiringExpanding = list()
RowsRequiringExpanding = list()
GalaxyLocations = list()

start = datetime.datetime.now()


for Row in range(Universe.shape[0]):
    for Col in range(Universe.shape[1]):
        # print(Universe[Row][Col])
        if Universe[Row][Col] != ".":
            break
    else:
        RowsRequiringExpanding.append(Row)

for Col in range(Universe.shape[1]):
    for Row in range(Universe.shape[0]):
        # print(Universe[Row][Col])
        if Universe[Row][Col] != ".":
            break
    else:
        ColsRequiringExpanding.append(Col)

for Col in ColsRequiringExpanding[::-1]:
    Universe = expandUniverse(Col, "y")

for Row in RowsRequiringExpanding[::-1]:
    Universe = expandUniverse(Row, "x")

for Row in range(Universe.shape[0]):
    for Col in range(Universe.shape[1]):
        if Universe[Row][Col] == "#":
            GalaxyLocations.append((Row, Col))

for index in range(len(GalaxyLocations)):
    output += measureGalaxyDistances(GalaxyLocations.pop())

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)