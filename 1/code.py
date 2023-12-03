input = "input.txt"
sum = 0

f = open(input, "r")

def getLineNumber(line):
    number = None
    for character in line:
        if character.isnumeric():
            number = character
            break
    return number

for line in f:
    number = getLineNumber(line) + getLineNumber(line[::-1])
    sum += int(number)
print(sum)
