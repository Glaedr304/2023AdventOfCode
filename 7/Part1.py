import datetime
from pprint import pprint
input = "input.txt"

camelCards = { "2":"00",
               "3":"01",
               "4":"02",
               "5":"03",
               "6":"04",
               "7":"05",
               "8":"06",
               "9":"07",
               "T":"08",
               "J":"09",
               "Q":"10",
               "K":"11",
               "A":"12"}

winningHands = {"11111":"1",
                "2111":"2",
                "221":"3",
                "311":"4",
                "32":"5",
                "41":"6",
                "5":"7"}

f = open(input, "r")

output = 0

hands = list()

for line in f:
    hands.append({str(line[:line.find(" ")]): None, "bid": int(line[line.find(" "):].strip())})

for listItem in hands:
    thisHand = list(listItem.keys())[0]
    listItem[thisHand] = {}
    for char in thisHand:
        if char in listItem[thisHand].keys():
            listItem[thisHand][char] += 1
        else:
            listItem[thisHand][char] = 1
pprint(hands)

def sortingKey(hand):
    key = "0"
    handCards = list(hand.keys())[0]

    sortedHand = sorted(list(hand[handCards].values()), reverse=True)
    
    sortedHandString = ""
    for num in sortedHand:
        sortedHandString += str(num)

    key = winningHands[sortedHandString]

    for char in handCards:
        key += camelCards[char]

    return int(key)

start = datetime.datetime.now()

hands.sort(key = sortingKey)
  

for handNumber in range(len(hands)):
    output += (handNumber + 1)*hands[handNumber]["bid"]

end = datetime.datetime.now() - start
print("Time: ", end)

print("Output: ", output)
