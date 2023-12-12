import datetime
input = "input.txt"

f = open(input, "r")

output = 0

data = list()

for line in f:
    data.append(line.strip())
f.close()

while '' in data:
    data.remove('')

rawSeeds = eval( "(" + data.pop(0).replace("seeds: ", "").replace(" ", ",") + ")")
seedRanges = set()
for x in range(int(len(rawSeeds)/2)):
    seedRanges.add(eval("range(" + str(rawSeeds[2*x])+ ", " + str(rawSeeds[2*x] + rawSeeds[2*x + 1]) + ")"))

maps = dict()
thisKey = -1
for row in data:
    if not row[0].isnumeric():
        thisKey += 1
        maps[thisKey] = list()
    if row[0].isnumeric():
        maps[thisKey].append(eval("(" + row.replace(" ", ",") + ")"))

upperBound = 331445006 # Solution to part 1

start = datetime.datetime.now()

for outputNumber in range(0, upperBound):
    originalOutput = outputNumber
    for map in list(maps.keys())[::-1]:
        for route in maps[map]:
            source = route[1]
            destination = route[0]
            numberRange = route[2]
            formalRange = range(destination, destination + numberRange)
            if outputNumber in formalRange:
                offset = outputNumber - destination
                outputNumber = source + offset
                break
        if map == 0:
            for seedRange in seedRanges:
                if outputNumber in seedRange:
                    print("originalOutput:", originalOutput)
                    print("outputNumber:", outputNumber)
                    output = originalOutput
                    break
            else:
                continue
            break
    else:
        continue
    break

o = open("output.txt", "a")
o.write(str(output))
o.close()

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)