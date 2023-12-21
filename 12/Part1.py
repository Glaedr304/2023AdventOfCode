import datetime
from pprint import pprint

inputFile = "input.txt"

output = 0

processed_input = []

with open(inputFile, 'r') as file:
    input_data = file.readlines()    
    for row in input_data:
        springs, group_str = row.strip().split()
        groups = list(map(int, group_str.split(',')))
        processed_input.append((springs, groups))

pprint(processed_input)


start = datetime.datetime.now()
end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
