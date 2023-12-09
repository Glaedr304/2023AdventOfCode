input = "input.txt"

output = 0

f = open(input, "r")
Cards = dict()

for line in f:
    card = int(line[line.find(" ") + 1:line.find(":")])
    line = line[line.find(":") + 1:].strip()

    WinningNumbers = eval( "(" + line[:line.find("|")].replace("  ", " ").strip().replace(" ", ",") + ")")
    Numbers = eval( "(" + line[line.find("|") + 1:].replace("  ", " ").strip().replace(" ", ",") + ")")

    Cards[card] = (WinningNumbers, Numbers)

winners = 0

def determineWinCount(card):
    winCount = 0
    print(Cards[card][0], Cards[card][1])
    for winner in Cards[card][0]:
        if winner in Cards[card][1]:
            winCount += 1
    print(card, winCount)
    return winCount

def loopThemCards(startCard):
    cards = 1
    count = determineWinCount(startCard)
    if count > 0:
        for i in range(startCard + 1, startCard + count):
            cards += loopThemCards(i)
    return cards

output = loopThemCards(1)


print("Output: ", output)

# 12973 too low
# 19460 too low
