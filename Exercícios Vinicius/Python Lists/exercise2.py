#COMANDO IN CHECA SE ALGO ESTÁ NA LISTA E DEVOLVE COMO BOOLEAN
# numbers = [1, 3, 5]
# print(5 in numbers)
# print(8 in numbers)
# print(5 not in numbers)
# print(8 not in numbers)

#COMANDO PARA PERCORRER TODOS OS ITENS DA LISTA
# cities = ["Chicago", "London", "Tokyo"]
# for city in cities:
#   print(city)

#COMANDO QUE ORGANIZA E PERCORRE TODOS OS ITENS DA LISTA ATE QUE CHEGE NA CONDIÇÃO
# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# numbers.sort()
# for number in numbers:
#   if number > 42:
#     break
#   print(number)

#ADICIONA NUMEROS ALEATORIOS NA LISTA DE 1 A 100 ATÉ QUE TENHAM 5 ITENS NA LISTA
#CASO ALGUM NUMERO SEJA 90 OU MAIS QUEBRA O LOOP
# import random
# numbers = []
# while len(numbers) < 5:
#   numbers.append(random.randint(1, 100))
# for number in numbers:
#   print(number)
#   if number >= 90:
#     print('Found at least one number greater than 90')
#     break
# else:
#   print('No numbers greater than 90')
# print('Complete')

#PERMUTA ITENS DE UMA LISTA PARA OUTRA USANDO IS INSTANCE
# values = ["laptop", 7, "phone", 3, "dslr", 5]
# equipment = []
# for value in values:
#   if isinstance(value, str) == False:
#     continue
#   equipment.append(value)
# print(equipment)

#MOSTRA TODAS AS COMBINAÇÕES DE LISTAS
# suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
# ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
# for  suit in suits:
#   for rank in ranks:
#     print(f'{rank} of {suit}')

#MOSTRA O COMANDO RANDOM.CHOICE(S) QUE ESCOLHE UM ITEM ALEATORIO DA LISTA
# import random
# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# selected_number = random.choice(numbers)
# print(selected_number)
# selected_numbers = random.choices(numbers, k=3)
# print(selected_numbers)
