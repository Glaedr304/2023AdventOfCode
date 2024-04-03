import numpy as np
import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

input = [x.split("\n") for x in f.read().split("\n\n")]

for puzzleIndex in range(len(input)):
    for rowIndex in range(len(input[puzzleIndex])):
        input[puzzleIndex][rowIndex] = [*input[puzzleIndex][rowIndex]]

output = 0

def validateMirror(arr, index, spacing, acceptableErrors) -> bool:
    minIndex = 0
    maxIndex = len(arr) - 1
    if (index < minIndex) or ((index + spacing + 1) > maxIndex): 
        if acceptableErrors == 0:
            return True
        return False
    
    firstNum = int(("".join(arr[index])).replace("#", "0").replace(".", "1"))
    secondNum = int(("".join(arr[index + spacing + 1])).replace("#", "0").replace(".", "1"))
    numRepresentation = str(abs(firstNum - secondNum)).replace("0", "")

    if numRepresentation == '': numRepresentation = 0
    else: numRepresentation = int(numRepresentation)

    # print(spacing, ":", firstNum, "-", secondNum, "=", numRepresentation)

    if numRepresentation > acceptableErrors:
        return False
    return validateMirror(arr, index - 1, spacing + 2, acceptableErrors - numRepresentation)

start = datetime.datetime.now()

for pattern in input:
    arr = np.array(pattern)

    breakFlag = True

    for colIndex in range(len(arr)):
        isMirror = validateMirror(arr, colIndex, 0, 1)
        print(colIndex, ":", isMirror)
        if isMirror == True: 
            output += (colIndex + 1)*100
            break
    else: breakFlag = False

    if breakFlag == True: 
        print("Breaking...")
        continue

    for rowIndex in range(len(np.transpose(arr))):
        isMirror = validateMirror(np.transpose(arr), rowIndex, 0, 1)
        if isMirror == True: 
            output += (rowIndex + 1)*1
            break

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)

# 22164 too low
# 73500 too high
# has to be less than 32723 original answer to part 1?
