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
    seedRanges.add("range(" + str(rawSeeds[2*x])+ ", " + str(rawSeeds[2*x] + rawSeeds[2*x + 1]) + ")")

for range1 in seedRanges:
    print(range1)

maps = dict()
thisKey = -1
for row in data:
    if not row[0].isnumeric():
        thisKey += 1
        maps[thisKey] = list()
    if row[0].isnumeric():
        maps[thisKey].append(eval("(" + row.replace(" ", ",") + ")"))

smallestTransformedSeed = 9999999999999999999999999999999
upperBound = 331445006 # Solution to part 1

start = datetime.datetime.now()

for seeds in seedRanges:
    for seed in eval(seeds):
        for map in maps.keys():
            for route in maps[map]:
                source = route[1]
                destination = route[0]
                numberRange = route[2]
                formalRange = range(source, source + numberRange)
                if seed in formalRange:
                    offset = seed - source
                    seed = destination + offset
                    break
        if seed < upperBound:
            smallestTransformedSeed = seed

output = smallestTransformedSeed

o = open("output.txt", "a")
o.write(str(output))
o.close()

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)

# 51359249 too low
# 331445006
# 239755573 too high
