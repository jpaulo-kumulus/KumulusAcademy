import random
##Exitem 52 cartas no total
##Existem 4 naipes no jogo: espadas, copas, paus, ouro
##Existem alguns tipos de cartas: 2, 3, 4, 5, 6, 7, 8, 9, 10, ás, valete, dama e rei
count = 0
auxList = []
auxListForPlayer = []
randomNumber = 0
naipes = ['Espadas', 'Copas', 'Paus', 'Ouro']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Aas', 'Valete', 'Dama', 'Rei']
auxTestVector = []

#print(naipes)
#print(values)

for finalNaipes in naipes:
    for finalValues in values:
        auxList.append(f' {finalValues} de {finalNaipes} ')

#print(auxList)
#print(len(auxList))
quantityOfCards = str(len(auxList))
#print('There are ' + quantityOfCards + ' cards in the deck')

while count != 5:
    randomNumber = random.randint(0, 51)
    auxListForPlayer = auxList.pop(randomNumber)
    print(auxListForPlayer)
    auxTestVector.append(auxListForPlayer)
    count = count + 1
#print(count)

print(auxList)
print(len(auxList))
print(auxListForPlayer)
print(auxTestVector)
