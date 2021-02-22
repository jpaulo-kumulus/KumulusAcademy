import random
rolls = 1
rightNumber = 0
rightNumber = random.randint(1, 5)
print(rightNumber) ##Tá saindo como inteiro

print('Guess a number between 1 and 5: ')
userChoice = input() ##Tá saindo como string
#print(userChoice.isnumeric())

while str(rightNumber) != userChoice:
    rolls = rolls + 1
    print('Guess a number between 1 and 5:')    
    if userChoice.isnumeric() == False:
        #rolls = rolls + 1
        userChoice = input()
    elif userChoice == '':
        #rolls = rolls + 1
        userChoice = input()
    else:
        #rolls = rolls + 1
        userChoice = input()
print(f'You guessed it in {rolls} times!')




#print(type(rightNumber))
#print(type(userChoice))
#if rightNumber == userChoice:
#    print('nice')
#else:
#    print('f')