import random 

number = random.randint(1,5)
count = 0
guess = 0

while guess!=number:
    guess = input("Guess a number between 1 and 5: ")
    count += 1
else:
    print(f'You guess it in {count} tries!')
