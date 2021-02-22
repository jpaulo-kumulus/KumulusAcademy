# import random MEU CÓDIGO
# roll = random.randint(1, 5)
# roll = str(roll)
# count = 1

# guess = input('Chute um numero de 1 a 5: ')

# while roll != guess:
#     print('Você errou, tente novamente: ')
#     guess = input()
#     count += 1

# print(f'Você acertou em {count} tentativas. O número era {roll}')
    
import random

value = random.randint(1, 5)
count = 0
guess = 0
while guess != value:
    count += 1
    guess = input('Guess a number between 1 and 5: ')
    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'You guessed it in {count} tries!')