import datetime
from pprint import pprint

inputFile = "input.txt"

output = 0

processed_input = []

with open(inputFile, 'r') as file:
    input_data = file.readlines()    
    for row in input_data:
        field, springGroups = row.strip().split()
        groups = [ int(x) for x in springGroups.split(',') ]
        # list(map(int, springGroups.split(',')))
        processed_input.append((field, groups))

# pprint(processed_input)

def checkTile(thisField, theseSprings, fieldIndex, springIndex, currentSpringLength):
    #below if checks if we have gotten to the end and used up our springs for a given field
    if fieldIndex == len(thisField):
        if springIndex == len(theseSprings) and currentSpringLength == 0:
            return 1
        elif springIndex == len(theseSprings) - 1 and theseSprings[springIndex] == currentSpringLength:
            return 1
        else:
            return 0
    
    # tally the future possible combinations
    possibleCombinations = 0
    for groundTile in [".", "#"]:
        if thisField[fieldIndex] == groundTile or thisField[fieldIndex] == "?":
            if groundTile == "." and currentSpringLength == 0:
                possibleCombinations += checkTile(thisField, theseSprings, fieldIndex + 1, springIndex, currentSpringLength)

            elif groundTile == "." and currentSpringLength > 0 and springIndex < len(theseSprings) and theseSprings[springIndex] == currentSpringLength:
                possibleCombinations += checkTile(thisField, theseSprings, fieldIndex + 1, springIndex + 1, 0)

            elif groundTile == "#":
                possibleCombinations += checkTile(thisField, theseSprings, fieldIndex + 1, springIndex, currentSpringLength + 1)
    return possibleCombinations

start = datetime.datetime.now()

for line in processed_input:

    Field = line[0]
    Springs = line[1]
    print(field, Springs)
    output += checkTile( Field, Springs, 0, 0, 0)

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
