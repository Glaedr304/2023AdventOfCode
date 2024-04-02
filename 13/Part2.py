import numpy as np
import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

input = [x.split("\n") for x in f.read().split("\n\n")]

for puzzleIndex in range(len(input)):
    for rowIndex in range(len(input[puzzleIndex])):
        input[puzzleIndex][rowIndex] = [*input[puzzleIndex][rowIndex]]

output = 0

def findDuplicates(arr, acceptableErrors): # I believe I can simplify this code and eliminate this function by passing a spacing of 0 to Validate Mirror
    matchesList = list()
    for rowIndex in range(len(arr) - 1):
        if "".join(arr[rowIndex]) == "".join(arr[rowIndex + 1]):
            matchesList.append(rowIndex)
    return matchesList

def validateMirror(arr, index, spacing, acceptableErrors) -> bool:
    minIndex = 0
    maxIndex = len(arr) - 1
    if (index - 1) < minIndex or (index + spacing) > maxIndex: 
        return True
    
    numRepresentation = abs(int(("".join(arr[index - 1])).replace("#", "0").replace(".", "1")) - int(("".join(arr[index + spacing])).replace("#", "0").replace(".", "1")))

    # print(("".join(arr[index - 1])).replace("#", "0").replace(".", "1"), "-", ("".join(arr[index + spacing])).replace("#", "0").replace(".", "1"), "=", numRepresentation)

    if str(numRepresentation).count("1") > acceptableErrors:
        return False
    return validateMirror(arr, index - 1, spacing + 2, acceptableErrors - int(str(numRepresentation).count("1")))

start = datetime.datetime.now()

for pattern in input:
    arr = np.array(pattern)

    for colIndex in range(len(np.transpose(arr))):
        isMirror = validateMirror(np.transpose(arr), colIndex, 0, 1)
        if isMirror == True: 
            output += colIndex + 1
            break

    for rowIndex in range(len(arr)):
        isMirror = validateMirror(arr, rowIndex, 0, 1)
        if isMirror == True: 
            output += 100*(rowIndex + 1)
            break


end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)

# 22164 too low
