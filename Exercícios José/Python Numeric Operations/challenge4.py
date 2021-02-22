print("What is the temperature in fahrenheit?")
fahrenValue = input()

if fahrenValue.isnumeric() == False:
    print('Imput is not a number')
    exit()
else:
    fahrenValue = int(fahrenValue)
    celsiusValue = ((fahrenValue - 32) * (5 / 9))
    celsiusValue = round(celsiusValue)
    #print(celsiusValue)
    print("Temperature in celsius is: " + str(celsiusValue))