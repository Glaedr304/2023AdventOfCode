import numpy as np
import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

input = [x.split("\n") for x in f.read().split("\n\n")]

for puzzleIndex in range(len(input)):
    for rowIndex in range(len(input[puzzleIndex])):
        input[puzzleIndex][rowIndex] = [*input[puzzleIndex][rowIndex]]

output = 0

def findDuplicates(arr):
    matchesList = list()
    for rowIndex in range(len(arr) - 1):
        if "".join(arr[rowIndex]) == "".join(arr[rowIndex + 1]):
            matchesList.append(rowIndex)
    return matchesList

def validateMirror(arr, index, spacing) -> bool:
    minIndex = 0
    maxIndex = len(arr) - 1
    if (index - 1) < minIndex or (index + spacing) > maxIndex: 
        return True
    if "".join(arr[index - 1]) != "".join(arr[index + spacing]):
        return False
    return validateMirror(arr, index - 1, spacing + 2)

start = datetime.datetime.now()

for pattern in input:
    arr = np.array(pattern)
    patternDict = {
        "columnIndexes": findDuplicates(np.transpose(arr)),
        "rowIndexes": findDuplicates(arr) 
        }
    if len(patternDict["columnIndexes"]) + len(patternDict["rowIndexes"]) == 1:
        # find the index, add it to the output and continue
        if patternDict["columnIndexes"] != []: 
            output += patternDict["columnIndexes"][0] + 1
        else:
            output += 100*(patternDict["rowIndexes"][0] + 1)
        continue
    
    isMirror = False

    if len(patternDict["columnIndexes"]) > 0:
        for colIndex in patternDict["columnIndexes"]:
            isMirror = validateMirror(np.transpose(arr), colIndex, 2)
            if isMirror == True: 
                output += colIndex + 1
                break

    if (len(patternDict["rowIndexes"]) > 0) and (isMirror != True):
        for rowIndex in patternDict["rowIndexes"]:
            isMirror = validateMirror(arr, rowIndex, 2)
            if isMirror == True: 
                output += 100*(rowIndex + 1)
                break


end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
