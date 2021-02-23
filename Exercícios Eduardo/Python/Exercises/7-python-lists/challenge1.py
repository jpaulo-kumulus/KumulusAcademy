import random

count = 0
deck = []
naipes = ["Hearts", "Spades", "Clubs", "Diamonds"]
numbers =  ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for naipe in naipes:
    for number in numbers:
        card = f'{number} of {naipe}'
        deck.append(card)
        count += 1

print('There are ', count, 'cards in the deck.')
print('Dealing ...')

hand = []

while len(hand) < 5:
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)