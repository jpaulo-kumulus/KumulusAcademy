#MOSTRA COMO CHAMAR UM MÓDULO (BASICAMENTE OUTRO CÓDIGO COM UMA OU MAIS FUNÇÕES QUE AUXILIA O CÓDIGO ATUAL)
import deck

cards = deck.create_deck()

for card in cards:
  print(card)