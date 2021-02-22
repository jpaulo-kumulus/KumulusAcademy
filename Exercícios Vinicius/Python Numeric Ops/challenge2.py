# MEU CÓDIGO
# print('Calculadora simples')

# num1 = input('Primeiro número: ')
# if num1.isnumeric() == False:
#     print('Você não digitou um número válido')
#     exit()
# num1 = int(num1)

# operador = input('Qual operação: ?\n"+" = Soma\n"-" = Diferença\n"*" = Produto\n"/" = Divisão\n"**" = Expoente\n"%" = Módulo\n')
# if operador != '+' and operador != '-' and operador != '*' and operador != '/' and operador != '**' and operador != '%':
#     print('Operador inválido')
#     exit()

# num2 = input('Segundo número: ')
# if num2.isnumeric() == False:
#     print('Você não digitou um número válido')
#     exit()
# num2 = int(num2)

# if operador == '+':
#     soma = num1 + num2
#     print('Total:' +str(soma))
# elif operador == '-':
#     dif = num1 - num2
#     print('Total:' +str(dif))
# elif operador == '*':
#     prod = num1 * num2
#     print('Total:' +str(prod))
# elif operador == '/':
#     division = num1 / num2
#     print('Total:' +str(division))
# elif operador == '%':
#     modulo = num1 % num2
#     print('Total:' +str(modulo))
# elif operador == '**':
#     expo = num1 ** num2
#     print('Total:' +str(expo))
# else:
#     print('Resultado inválido')

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