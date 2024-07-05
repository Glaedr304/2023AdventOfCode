import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

listToHash = f.read().split(",", -1)
hashedList = list()

output = 0

def hashFunction(var: str, val: int):
    return 17*(ord(var) + val)%256

start = datetime.datetime.now()

for item in listToHash:
    Value = 0
    for char in item:
        Value = hashFunction(char, Value)
    hashedList.append(Value)

output =sum(hashedList)

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
