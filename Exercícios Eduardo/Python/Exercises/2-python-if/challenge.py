
resp = input('Would you like to continue? ')

if resp == 'n' or resp == 'no':
    print('Exiting')
elif resp == 'y' or resp == 'yes':
    print('Continuing ...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no.')
