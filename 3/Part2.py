import numpy as np

input = "input.txt"

PartNumber = 0

f = open(input, "r")

Numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
Gear = {"*"}

lines = list() # to be later converted to a touple

for line in f:
    characters = tuple()
    for character in line:
        characters += tuple(character)
    lines.append(characters)
lines = tuple(lines)
arr = np.transpose(np.array(lines))

def checkAroundGear(x, y):
    orderH = (0, -1, 1)
    orderV = (-1, 0, 1)

    numCount = 0

    for y2 in orderV:
        for x2 in orderH:
            if str(arr[x + x2][y + y2]) in Numbers:
                pass
                numCount += 1
                if numCount >= 2:
                    return True
                if x2 == 0:
                    break
    return False

def getNumber(x, y):
    print()
    number = 1
    placeholderString = ""

    orderH = (-3, -2, -1, 0, 1, 2, 3)
    orderV = (-1, 0, 1)

    wasAroundGearFlag = False

    for y2 in orderV:
        for x2 in orderH:
            print(arr[x + x2][y + y2], end=" ")
            if not arr[x + x2][y + y2].isnumeric() and placeholderString == "":
                pass
            elif not arr[x + x2][y + y2].isnumeric() and placeholderString != "" and not wasAroundGearFlag:
                placeholderString = ""
            elif not arr[x + x2][y + y2].isnumeric() and wasAroundGearFlag:
                number *= int(placeholderString)
                placeholderString = ""
                wasAroundGearFlag = False
            elif arr[x + x2][y + y2].isnumeric() and x2 in orderV:
                wasAroundGearFlag = True
                placeholderString += arr[x + x2][y + y2]
            elif arr[x + x2][y + y2].isnumeric() and x2 == 3 and wasAroundGearFlag:
                placeholderString += arr[x + x2][y + y2]
                number *= int(placeholderString)
                placeholderString = ""
                wasAroundGearFlag = False
            elif arr[x + x2][y + y2].isnumeric():
                placeholderString += arr[x + x2][y + y2]
            else:
                print("Shouldnt have got here")
        placeholderString = ""
        print("")
    print("Number: ", number)
    return number

for y in range(arr.shape[1]):
    for x in range(arr.shape[0]):
        if arr[x][y] in Gear:
            if checkAroundGear(x, y):
                PartNumber += getNumber(x, y)

print("Part Number: ", PartNumber)
