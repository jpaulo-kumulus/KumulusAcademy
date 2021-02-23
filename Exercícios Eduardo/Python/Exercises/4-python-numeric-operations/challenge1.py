

fahrenheit = input("What is the temperature in fahrenheit? " )

if fahrenheit.isnumeric()==False:
    print("Input is not a number.")
    exit()

celsius = (int(fahrenheit) - 32) * 5/9
print("temperature in celsius is ", int(celsius))
