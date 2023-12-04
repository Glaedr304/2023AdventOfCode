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

# print(list(textNumbers.keys())[-1])

for x in textNumbers.keys():
    wordString += x
    # print(len(textNumbers))
    # print(textNumbers[9])
    # print(x)
    if x != list(textNumbers.keys())[-1]:
        # print(x)
        wordString += "|"

# print(wordString)

f = open(input, "r")

def getLineNumber(line):
    number = None
    characters = ""
    for character in line:
        characters += character
        # print("characters: ", characters)
        if character.isnumeric():
            number = character
            print("number: ", number)
            break
        elif re.search(wordString, characters) != None:
            Match = re.search(wordString, characters)
            print("match: ", str(Match.string[Match.start():Match.end()]))
            print("Dict Value: ", textNumbers[str(Match.string[Match.start():Match.end()])])
            # number = str(textNumbers[Match.string[Match.start():Match.end()]])
            number = str(textNumbers[str(Match.string[Match.start():Match.end()])])
            break
        elif re.search(wordString[::-1], characters) != None:
            Match = re.search(wordString[::-1], characters)
            print("Match String: ", Match.string)
            # print("reverse match: ", str(Match.string)[::-1])
            print("reverse match: ", str(Match.string[Match.start():Match.end()])[::-1])
            print("Dict Reverse Value: ", textNumbers[str(Match.string[Match.start():Match.end()])[::-1]])
            # number = str(textNumbers[str(Match.string[Match.start():Match.end():-1]])
            number = str(textNumbers[str(Match.string[Match.start():Match.end()])[::-1]])
            break

    return number

for line in f:
    line = line.strip()
    print("line: ", line)
    number = getLineNumber(line) + getLineNumber(line[::-1])
    sum += int(number)
print(sum)
