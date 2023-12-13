import datetime
from pprint import pprint
input = "input.txt"

camelCards = { "J":"00",
               "2":"01",
               "3":"02",
               "4":"03",
               "5":"04",
               "6":"05",
               "7":"06",
               "8":"07",
               "9":"08",
               "T":"09",
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
    # TODO add code for removing J and adding it to the largest other card here
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
