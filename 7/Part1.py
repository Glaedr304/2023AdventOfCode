import datetime
from pprint import pprint
input = "input.txt"

camelCards = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
winningHands = ("11111", "2111", "221", "311", "32", "41", "5")

f = open(input, "r")

output = 0

hands = list()

for line in f:
    hands.append({str(line[:line.find(" ")]): None, "bid": int(line[line.find(" ") + 1:line.find("\n")])})

for listItem in hands:
    thisHand = list(listItem.keys())[0]
    listItem[thisHand] = {}
    for char in thisHand:
        if char in listItem[thisHand].keys():
            listItem[thisHand][char] += 1
        else:
            listItem[thisHand][char] = 1
pprint(hands)

start = datetime.datetime.now()



end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
