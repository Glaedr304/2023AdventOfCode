import datetime
import math

input = "input.txt"

f = open(input, "r")

output = 1

data = dict()

for line in f:
    data[line[:line.find(":")]] = line[line.find(":") + 1:]

previousNumber = False
newData = ""

for key in data.keys():
    data[key] = int(data[key].strip().replace(" ", ""))
print(data)


def quadraticFormula(a, b, c):
    return ((-b + ((b*b - 4*a*c)**(1/2)))/(2*a), (-b - ((b*b - 4*a*c)**(1/2)))/(2*a))

start = datetime.datetime.now()

a = -1
b = data["Time"]
c = -data["Distance"]
firstTimeHeld = quadraticFormula(a, b, c)

output *= (math.floor(firstTimeHeld[1]) - math.ceil(firstTimeHeld[0]) + 1)

end = datetime.datetime.now() - start

print("Time: ", end)

print("Output: ", output)