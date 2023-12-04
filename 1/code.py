input = "input.txt"
sum = 0
# print(list(textNumbers.keys())[-1])

    # print(len(textNumbers))
    # print(textNumbers[9])
    # print(x)
        # print(x)

# print(wordString)

f = open(input, "r")

def getLineNumber(line):
    number = None
    for character in line:
        # print("characters: ", characters)
        if character.isnumeric():
            number = character
            break
            print("match: ", str(Match.string[Match.start():Match.end()]))
            print("Dict Value: ", textNumbers[str(Match.string[Match.start():Match.end()])])
            # number = str(textNumbers[Match.string[Match.start():Match.end()]])
            print("Match String: ", Match.string)
            # print("reverse match: ", str(Match.string)[::-1])
            print("reverse match: ", str(Match.string[Match.start():Match.end()])[::-1])
            print("Dict Reverse Value: ", textNumbers[str(Match.string[Match.start():Match.end()])[::-1]])
            # number = str(textNumbers[str(Match.string[Match.start():Match.end():-1]])
    return number

for line in f:
    number = getLineNumber(line) + getLineNumber(line[::-1])
    sum += int(number)
print(sum)
