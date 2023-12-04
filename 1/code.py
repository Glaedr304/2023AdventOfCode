import re

input = "input.txt"
sum = 0
textNumbers = {
    "zero": 0,
    "one":  1,
    "two":  2,
    "three":3,
    "four": 4,
    "five": 5,
    "six":  6,
    "seven":7,
    "eight":8,
    "nine": 9,
    }

wordString = ""

for x in textNumbers.keys():
    wordString += x
    if x != list(textNumbers.keys())[-1]:
        wordString += "|"

f = open(input, "r")

def getLineNumber(line):
    number = None
    characters = ""
    for character in line:
        characters += character
        if character.isnumeric():
            number = character
            break
        elif re.search(wordString, characters) != None:
            Match = re.search(wordString, characters)
            number = str(textNumbers[str(Match.string[Match.start():Match.end()])])
            break
        elif re.search(wordString[::-1], characters) != None:
            Match = re.search(wordString[::-1], characters)
            number = str(textNumbers[str(Match.string[Match.start():Match.end()])[::-1]])
            break
    return number

for line in f:
    line = line.strip()
    number = getLineNumber(line) + getLineNumber(line[::-1])
    sum += int(number)
print(sum)
