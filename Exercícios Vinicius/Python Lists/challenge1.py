import random

suits = ["Copas", "Espadas", "Paus", "Ouro"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Às"]
deck = []

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} de {suit}')

print(f'Tem {len(deck)} cartas no seu baralho!')

print('Dealing...')

hand = []

while len(hand) < 5:
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

print(f'Tem {len(deck)} cartas no seu baralho!')

print(f'O jogador está com {hand} na mão')

print(f'Sobraram as seguintes no baralho {deck}')