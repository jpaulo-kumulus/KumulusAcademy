print('Welcome to the Challenge 2!')
print('Would you like to continue?')
firstAnswer = input()

if firstAnswer == 'no' or firstAnswer == 'n':
    print("Exiting!")
elif firstAnswer == 'yes' or firstAnswer == 'y':
    print("Continuing...")
    print("Complete!")
else:
    print("Please try again and respond with yes or no")