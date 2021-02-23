# celsius = (fahrenheit - 32) * 5/9 fórmula de conversão

temp = input('Qual a temperatura em Farhenheit? ')
if temp.isnumeric() == False:
    print('Você não digitou um número válido')
    exit()
temp = float(temp)
celsius = (temp - 32) * (5/9)
print('Temperatura em Celsius: ' +str(celsius))