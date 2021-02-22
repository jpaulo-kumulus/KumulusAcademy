# import random MEU CÓDIGO
# roll = random.randint(1, 10)
# guess = 0
# guess_count = 0

# print('Chute um número de 1 a 10!\n')

# while roll != guess:
#     guess_count += 1
#     guess = input(f'Tentativa #{guess_count}\n')
#     if guess.isnumeric()==False:
#         print('Apenas números, por favor!')
#         continue
#     guess = int(guess)
#     if guess < roll:
#         print('Seu chute foi menor que o número')
#         continue
#     elif guess > roll:
#         print('Seu chute foi maior que o número')
#         continue
    
# print(f'Você acertou em {guess_count} tentativas. O número era {roll}')

import random

value = random.randint(1, 10)
count = 0
guess = 0
print('Guess a number between 1 and 10')

while guess != value:
    count += 1
    guess = input(f'Enter guess #{count}: ')

    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue

    if guess > value:
        print('Your guess is too high, try again!')
    elif guess < value:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {count} tries!')