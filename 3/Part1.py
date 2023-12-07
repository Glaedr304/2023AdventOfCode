import numpy as np

input = "input.txt"

PartNumber = 0

f = open(input, "r")

AllCharacters = set() # readying the set

Numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
NotCharacters = Numbers.union({".", "\n"})

Characters = set() # AllCharacters - NotCharacters

lines = list() # to be later converted to a touple

for line in f:
    characters = tuple()
    for character in line:
        characters += tuple(character)
        if character in AllCharacters:
            pass
        else:
            AllCharacters.add(character)
    # print("characters: ", characters)
    lines.append(characters)
lines = tuple(lines)
# print("Lines:")
# print(lines)
arr = np.transpose(np.array(lines))
# arr = np.delete(arr, arr.shape[1], 0)

Characters = AllCharacters
for character in NotCharacters:
    try:
         Characters.remove(character)
    except:
        pass
# print("Characters: ", Characters)

# print("Line: ", lines[0][1], lines[0][2], lines[0][3])



def getNextCharacters(x, y):
    # print("Next Character: ", lines[x][y + 1])
    if arr[x + 1][y].isnumeric():
        # print("Next Character:", lines[x + 1][y])
        return str(arr[x][y]) + getNextCharacters(x + 1, y)
    else:
        return str(arr[x][y])

def checkAroundNumber(x, y, numLength):

    xmin = x - 1
    xmax = x + numLength + 1
    ymin = y - 1
    ymax = y + 1
    print("xmax - xmin", xmax - xmin)
    print("ymax - ymin", ymax - ymin)
    print("x,y", x, y, "xmin", xmin, "xmax", xmax, "ymin", ymin, "ymax", ymax)
    if xmin < 0:
        xmin += 1
    if xmax >= arr.shape[0]:
        xmax -= 1
    if ymin < 0:
        ymin += 1
    if ymax >= arr.shape[1]:
        ymax -= 1

    for y2 in range(ymin, ymax+1):
        for x2 in range(xmin, xmax):
            print(x2, y2, arr[x2][y2], end=" ")
            if str(arr[x2][y2]) in Characters:
                return True
            # print(x2, y2, arr[x2][y2])
        print("")
    return False

for y in range(arr.shape[1]):
    skipNumber = 0
    for x in range(arr.shape[0]):
        # print("x, y", x, y)
        if skipNumber > 0:
            skipNumber -= 1
            continue
        if arr[x][y].isnumeric():
            Number = getNextCharacters(x, y)
            print("Number", Number)
            if checkAroundNumber(x, y, len(Number)):
                PartNumber += int(Number)
            skipNumber = len(Number) - 1

# print(arr)
# print(arr.shape)
print("Part Number: ", PartNumber)
