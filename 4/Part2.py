import datetime
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
    for winner in Cards[card][0]:
        if winner in Cards[card][1]:
            winCount += 1
    return winCount

def loopThemCards(startCard, loopDepth):
    cards = 1
    count = determineWinCount(startCard)
    if count == 1:
        cards += loopThemCards(startCard + 1, loopDepth + 1)
    if count > 1:
        for i in range(startCard + 1, startCard + 1 + count):
            cards += loopThemCards(i, loopDepth + 1)
    return cards


start = datetime.datetime.now()
for i in range(1, list(Cards.keys())[-1] + 1):
    output += loopThemCards(i, 0)
end = datetime.datetime.now() - start


print("Time: ", end)
print("Output: ", output)
