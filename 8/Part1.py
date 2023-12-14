import datetime

input = "input.txt"

f = open(input, "r")

Start = 'AAA'
WhereIAm = Start
End = 'ZZZ'

output = 0

Directions = f.readline().replace("L", "0").replace("R", "1").strip()
print("Directions Length:", len(Directions))
f.readline()

Map = dict()

for line in f:
    string1 = line[line.find("(") + 1:line.find(",")].strip()
    string2 = line[line.find(",") + 1:line.find(")")].strip()

    Map[line[:line.find(" ")]] = (string1, string2)

def Navigate(place, dir):
    return Map[place][dir]

start = datetime.datetime.now()

steps = 0

while WhereIAm != End:

    for num in Directions:
        WhereIAm = Navigate(WhereIAm, int(num))
        steps += 1

print("Where I am:", WhereIAm)
output = steps

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)