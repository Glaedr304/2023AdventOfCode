import datetime

input = "input.txt"

f = open(input, "r")

output = 0

Directions = f.readline().replace("L", "0").replace("R", "1").strip()
print("Directions Length:", len(Directions))

f.readline()

Map = dict()

Start = list()

for line in f:
    node = line[:line.find(" ")]
    string1 = line[line.find("(") + 1:line.find(",")].strip()
    string2 = line[line.find(",") + 1:line.find(")")].strip()
    Map[node] = (string1, string2)
    if node[-1] == 'A':
        Start.append(node)

WhereIAm = Start
print("Where I Start", WhereIAm)

def Navigate(place, dir):
    return Map[place][dir]

def TestZs(places):
    for node in places:
        if node[-1] != 'Z':
            break
    else:
        return False
    return True

animation = "|/-\\"

start = datetime.datetime.now()

steps = 0
idx = 0

while TestZs(WhereIAm):
    if str(steps)[-1] == "0":
        print(animation[idx % len(animation)], end="\r")
        idx += 1
    for index in Directions:
        # print(index, WhereIAm)
        for node in range(len(WhereIAm)):
            WhereIAm[node] = Navigate(WhereIAm[node], int(index))
        steps += 1

print("Where I am:", WhereIAm)
output = steps

end = datetime.datetime.now() - start

o = open("output.txt", "a")
o.write(str(output))
o.close()

print("Time: ", end)

print("Output: ", output)