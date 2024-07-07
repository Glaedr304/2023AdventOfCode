import datetime
from pprint import pprint 

output = 0

inputFile = "input2.txt"

f = open(inputFile, "r")

mirrorMap = f.read().split("\n")

energizerMap = list()
for index in range(len(mirrorMap)*len(mirrorMap[0])):
    energizerMap.append(".")

# pprint(mirrorMap)

class Beam:
    def __init__(self, x, y, Dir):
        self.Dir: str = Dir
        self.x: int = x
        self.y: int = y

beamStack = [
        Beam(-1, 0, "E")
    ]

def moveBeam(Dir: str) -> None: 
    if   Dir == "N":
        beamStack[0].y -= 1     
    elif Dir == "E":
        beamStack[0].x += 1 
    elif Dir == "S":
        beamStack[0].y += 1 
    elif Dir == "W":
        beamStack[0].x -= 1 
    else:
        print("fuck, how did you get here?")
    
    if beamStack[0].x < 0 or beamStack[0].y < 0 or beamStack[0].x >= len(mirrorMap[0]) or beamStack[0].y >= len(mirrorMap):
        return None
    energize(beamStack[0].x, beamStack[0].y)

    thisChar = mirrorMap[beamStack[0].x][beamStack[0].y]

    if thisChar == ".":
        moveBeam(Dir)
    elif thisChar == "/" or thisChar == "\\":
        newBeamDir = {
            "/": {
                "N":"E",
                "W":"S",
                "E":"N",
                "S":"W"
            },
            "\\": {
                "N":"W",
                "W":"N",
                "E":"S",
                "S":"E"
            }
        }
        beamStack.append(Beam(beamStack[0].x, beamStack[0].y, newBeamDir[thisChar][Dir])) 

    elif thisChar == "|" or thisChar == "-":
        newBeamDir = {
            "|": {
                "N":["N"],
                "W":["N", "S"],
                "E":["N", "S"],
                "S":["S"]
            },
            "-": {
                "N":["E", "W"],
                "W":["W"],
                "E":["E"],
                "S":["E", "W"]
            }
        }
        for newDir in newBeamDir[thisChar]:
            beamStack.append(Beam(beamStack[0].x, beamStack[0].y, newDir))
    else:
        print("I shouldnt be here.")

def energize(xPos: int, yPos: int) -> None:
    energizerMap[yPos*len(mirrorMap) + xPos] = "#"

start = datetime.datetime.now()

while len(beamStack) != 0:
# for beam in beamStack:
    moveBeam(beamStack[0].Dir)

output = energizerMap.count("#")

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)
