import datetime
from pprint import pprint 

output = 0

inputFile = "input2.txt"

f = open(inputFile, "r")

mirrorMap = f.read().split("\n")

pprint(mirrorMap)

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

def moveBeam() -> None: 
    if   beamStack[0].Dir == "N":
        beamStack[0].y -= 1     
    elif beamStack[0].Dir == "E":
        beamStack[0].x += 1 
    elif beamStack[0].Dir == "S":
        beamStack[0].y += 1 
    elif beamStack[0].Dir == "W":
        beamStack[0].x -= 1 
    else:
        print("fuck, how did you get here?")
    
    # print("\r", beamStack[0].x, beamStack[0].y, end = "")
    if beamStack[0].x < 0 or beamStack[0].y < 0 or beamStack[0].x >= len(mirrorMap[0]) or beamStack[0].y >= len(mirrorMap):
        beamStack.pop(0)
        return None
    else:
        energize(beamStack[0].x, beamStack[0].y)

    thisChar = mirrorMap[beamStack[0].y][beamStack[0].x]
    print("This character is", thisChar, "at", beamStack[0].x, beamStack[0].y)

    if thisChar == ".":
        moveBeam()
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
        print("Before:", beamStack[0].x, ":", beamStack[0].y, ",", beamStack[0].Dir)
        beamStack[0].Dir = newBeamDir[thisChar][beamStack[0].Dir]
        print("After:", beamStack[0].x, ":", beamStack[0].y, ",", beamStack[0].Dir)
        moveBeam()
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
        print("Before:", beamStack[0].x, ":", beamStack[0].y, ",", beamStack[0].Dir)
        if len(newBeamDir[thisChar]) == 1:
            moveBeam()
        else:
            for newDir in newBeamDir[thisChar]:
                beamStack.append(Beam(beamStack[0].x, beamStack[0].y, newDir))
                beamStack.pop(0)
    else:
        print("I shouldnt be here.")

def energize(xPos: int, yPos: int) -> None:
    print("Energizing!")
    energizerMap[yPos*len(mirrorMap) + xPos] = "#"

start = datetime.datetime.now()

while len(beamStack) != 0:
# for beam in beamStack:
    print("This Beam:", beamStack[0].x, beamStack[0].y, beamStack[0].Dir)
    moveBeam()
    # print("\r", beamStack[0].x, beamStack[0].y, len(beamStack), end="")

output = energizerMap.count("#")

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)
