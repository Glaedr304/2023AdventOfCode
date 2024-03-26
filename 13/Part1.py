import numpy as np
import datetime

inputFile = "input.txt"

f = open(inputFile, "r")

input = [x.split("\n") for x in f.read().split("\n\n")]

output = 0

def findDuplicates(arr):
    print(arr)

start = datetime.datetime.now()

for pattern in input:
    # print(pattern)
    arr = np.array(pattern)
    findDuplicates(arr)
    # findDuplicates(np.transpose(arr))

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
