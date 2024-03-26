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
    # print(arr[0])
    for rowIndex in range(len(arr) - 1):
        # print(arr[rowIndex + 1])
        if "".join(arr[rowIndex]) == "".join(arr[rowIndex + 1]):
            # print(rowIndex)
            matchesList.append(rowIndex)
            # return rowIndex
    # if matchesList == list():
    #     # print("No Matches")
    #     return None
    # print(matchesList)
    return matchesList

def validateMirror(arr, index):
    pass

start = datetime.datetime.now()

for pattern in input:
    arr = np.array(pattern)
    patternDict = {
        "columnIndexes": findDuplicates(np.transpose(arr)),
        "rowIndexes": findDuplicates(arr) 
        }
    print(patternDict)


end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
