def create_deck_test():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck_test = []

  for  suit in suits:
    for rank in ranks:
      deck_test.append(f'{rank} of {suit}')

  return deck_test