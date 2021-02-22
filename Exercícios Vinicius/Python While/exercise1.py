#CONTAR QUANTAS VEZES ROLA UM DADO ATÉ ACERTAR COM WHILE
# import random 
# roll = 0
# count = 0
# while roll != 5:
#   count = count + 1
#   roll = random.randint(1, 5)
#   print(roll)
# print(f'It took {count} rolls to roll a 5!')

#LOOP DE COLOCAR O NOME ATÉ QUE ALGUEM ACERTE O NUMERO COM WHILE
# roll = 0
# count = 0
# print('First person to roll a 5 wins!')
# while roll != 5:
#   name = input('Enter a name, or \'q\' to quit:  ' )
#   if name == 'q':
#     break
#   count = count + 1
#   roll = random.randint(1, 5)
#   print(f'{name} rolled {roll}')
# else:
#     print(f'{name} Wins!!!')
# print(f'You rolled the dice {count} times.')

#COMANDO CONTINUE QUE MANTEM VOLTA PARA DENTRO DO WHILE E BREAK QUE SAI DO WHILE
# roll = 0
# count = 0

# print('First person to roll a 5 wins!')
# while roll != 5:
#   name = input('Enter a name, or \'q\' to quit:  ' )

#   if name.strip() == '':
#     continue

#   if name.strip() == 'q':
#       break
  
#   count = count + 1
#   roll = random.randint(1, 5)
#   print(f'{name} rolled {roll}')
# else:
#     print(f'{name} Wins!!!')

# print(f'You rolled the dice {count} times.')