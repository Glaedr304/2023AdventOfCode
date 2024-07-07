import datetime
from pprint import pprint 

output = 0

inputFile = "input.txt"

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

    def moveBeam(self, Dir: str) -> None: 
        if   Dir == "N":
            pass    
        elif Dir == "E":
            pass
        elif Dir == "S":
            pass
        elif Dir == "W":
            pass
        else:
            print("fuck, how did you get here?")

beamStack = [
        Beam(-1, 0, "E")
    ]



def energize(xPos: int, yPos: int) -> None:
    energizerMap[yPos*len(mirrorMap) + xPos] = "#"

start = datetime.datetime.now()

for beam in beamStack:
    beam.moveBeam(beam.Dir)

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)
