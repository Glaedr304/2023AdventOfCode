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

seeds = eval( "(" + data.pop(0).replace("seeds: ", "").replace(" ", ",") + ")")

maps = dict()

thisKey = -1
for row in data:
    if not row[0].isnumeric():
        thisKey += 1
        maps[thisKey] = list()
    if row[0].isnumeric():
        maps[thisKey].append(eval("(" + row.replace(" ", ",") + ")"))

transformedSeeds = list()

start = datetime.datetime.now()

for seed in seeds:
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
    transformedSeeds.append(seed)

end = datetime.datetime.now() - start

for x in range(len(seeds)):
    print("Seed:", seeds[x], "->", transformedSeeds[x])

output = min(transformedSeeds)

print("Time: ", end)

print("Output: ", output)

# 51359249 too low
# 331445006
