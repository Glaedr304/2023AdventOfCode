import datetime
from pprint import pprint 

inputFile = "input.txt"

f = open(inputFile, "r")

listToHash = f.read().split(",", -1)
hashedList = list()

output = 0

def hashFunction(var: str, val: int):
    return 17*(ord(var) + val)%256

start = datetime.datetime.now()

hashmap = dict()

for x in range(256):
    hashmap[str(x)] = dict()

for itemIndex in range(len(listToHash)):

    thisDict = {
        "label": "",
        "hash": -1,
        "operator": "",
        "lense": None
    }
    if listToHash[itemIndex].rfind("=") > 0:
        thisDict["label"] = listToHash[itemIndex][:listToHash[itemIndex].rfind("=")]
        thisDict["operator"] = "="
        thisDict["lense"] = listToHash[itemIndex][-1]
    elif listToHash[itemIndex].rfind("-") > 0:
        thisDict["label"] = listToHash[itemIndex][:listToHash[itemIndex].rfind("-")]
        thisDict["operator"] = "-"
    else:
        print("How the fuck did I get here?")
    Value = 0
    
    for char in thisDict["label"]:
        Value = hashFunction(char, Value)
    thisDict["hash"] = Value

    hashedList.append(thisDict)

for instruction in hashedList:
    thisHash = str(instruction["hash"])
    thisOperator = str(instruction["operator"])
    thisLabel = str(instruction["label"])
    thisLense = str(instruction["lense"])

    if thisOperator == "=":
        hashmap[thisHash][thisLabel] = thisLense

    elif thisOperator == "-":
        try:
            hashmap[thisHash].pop(thisLabel)
        except:
            pass
    else:
        print("How the fuck did I get here??")

for box in hashmap:
    boxIndex = eval(box)
    slotIndex = 1
    for slot in hashmap[box]:
        print(slot)
        print(type(hashmap[box][slot]))
        output += (boxIndex + 1)*(slotIndex)*int(hashmap[box][slot])
        slotIndex += 1

# pprint(hashmap)
end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)

# 244845 too low
# 413307 too high
# 245223 just right!