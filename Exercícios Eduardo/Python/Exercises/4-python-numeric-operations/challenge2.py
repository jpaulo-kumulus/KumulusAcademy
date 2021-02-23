first_number = input('Simple calculator! \n First number?')
operation = input('Operator?')
second_number = input('Second number?')

if first_number.isnumeric()==False or second_number.isnumeric==False:
    print("Please input a number.")
    exit()
elif operation!='+' and operation!='-' and operation!='*' and operation!='/' and operation!='**' and operation!='%':
    print('Operation not recognized.')
    exit()
else:
    result = int(first_number) operation int(second_number)
    print('product of', first_number, operation, second_number, 'equals', result, sep=' ')

# codigo esta errado

# *****************************************************************************************************

# codigo certo
print('Simple calculator!')

first_number = input('First number? ')

if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = input('Operation? ')

second_number = input('Second number? ')

if second_number.isnumeric() == False:
    print('Please input a number.')
    exit()

first_number = int(first_number)
second_number = int(second_number)

result = 0
if operation == '+':
    result = first_number + second_number
    label = 'sum'
elif operation == '-':
    result = first_number - second_number
    label = 'difference'
elif operation == '*':
    result = first_number * second_number
    label = 'product'
elif operation == '/':
    result = first_number / second_number
    label = 'quotient'
elif operation == '**':
    result = first_number ** second_number
    label = 'exponent'
elif operation == '%':
    result = first_number % second_number
    label = 'modulus'
else:
    print('Operation not recognized.')
    exit()

print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(result))