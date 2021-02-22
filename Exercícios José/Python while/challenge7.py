import random
rolls = 1##inteiro
rightNumber = random.randint(1, 10) ##inteiro
print(rightNumber)
print('Guess a number between 1 and 10:')
print('Enter guess #1: ')
usersChoice = input()##string
#print(type(usersChoice))
#print(type(rightNumber))
#print(type(rolls))

while str(rightNumber) != usersChoice:
    rolls = rolls + 1
    if usersChoice.isnumeric() == False:
        print('Numbers only, please')
        print('Enter guess #' + str(rolls))
    elif int(usersChoice) > int(rightNumber):
        print('Your guess is too high, try again')
    elif int(usersChoice) < int(rightNumber):
        print('Your guess is too low, try again')
    usersChoice = input()
print(f'You guessed it in {rolls} times!')



        
