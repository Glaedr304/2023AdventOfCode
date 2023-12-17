import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

output = 0

rows = f.read().splitlines()

for lineIndex in range(len(rows)):
    rows[lineIndex] = rows[lineIndex].split()

for rowIndex in range(len(rows)):
    for elementIndex in range(len(rows[rowIndex])):
        rows[rowIndex][elementIndex] = int(rows[rowIndex][elementIndex])

def isListZeros(myList):
    for item in myList:
        if item != 0:
            return True
    return False

def Triangulate(thisRow): # expandTriangles would also be an appropriate name
    differenceList = list()
    for index in range(1, len(thisRow)):
        differenceList.append(thisRow[index] - thisRow[index - 1])
    return differenceList

trianglesList = list()

start = datetime.datetime.now()

for pyramidBaseList in rows:
    thisPyramid = list()
    thisPyramid.append(pyramidBaseList)

    while isListZeros(thisPyramid[-1]):
        thisPyramid.append(Triangulate(thisPyramid[-1]))

    trianglesList.append(thisPyramid)

for pyramid in trianglesList:
    lastRowValue = 0
    for layerIndex in reversed(range(len(pyramid))):
        if not isListZeros(pyramid[layerIndex]):
            continue
        print("Last Row Value is", lastRowValue, "and left number is",  pyramid[layerIndex][0])
        lastRowValue = pyramid[layerIndex][0] - lastRowValue
    output += lastRowValue

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)

