import random

#make deck
suits = [' of Hearts',' of Clubs',' of Diamonds',' of Spades']
numbers = [str(i) for i in range(1,11)]
numbers = numbers + ['Ace', 'King', 'Queen', 'Jack']

deck = []
for s in suits:
    for n in numbers:
        deck.append(n + s)

print("ORIGINAL DECK")
print(deck)

#shuffle functions
def shuffle(deck):
    shuffled = []
    while(deck):
        i = random.randint(0, len(deck) - 1)
        shuffled.append(deck[i])
        deck.pop(i)
    return shuffled

deck = shuffle(deck)
print("NEW DECK")
print(deck)

