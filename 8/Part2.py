import datetime
from math import lcm

inputFile = "input.txt"

f = open(inputFile, "r")

output = 0

Directions = f.readline().replace("L", "0").replace("R", "1").strip()

f.readline()

Map = dict()

Start = list()

for line in f:
    node = line[:line.find(" ")]
    string1 = line[line.find("(") + 1:line.find(",")].strip()
    string2 = line[line.find(",") + 1:line.find(")")].strip()
    Map[node] = (string1, string2)
    if node[-1] == 'A':
        Start.append(node)

def Navigate(place, dir):
    return Map[place][dir]

def getSteps(myLocation):
    steps = 0
    while myLocation[-1] != "Z":
        for index in Directions:
            myLocation = Navigate(myLocation, int(index))
            steps +=1
    return steps

stepsToEachZ = list()

start = datetime.datetime.now()

for startLine in range(len(Start)):
    stepsToEachZ.append(getSteps(Start[startLine]))

output = lcm(stepsToEachZ[0], stepsToEachZ[1], stepsToEachZ[2], stepsToEachZ[3], stepsToEachZ[4], stepsToEachZ[5])

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)