print('Simple calculator!')
firstNumber = input()

if firstNumber.isnumeric() == False:
    print('Please input a number')
    exit()
else:
    secondNumber = input()
    if secondNumber.isnumeric() == False:
            print('Please input a number')
            exit()
    else:
            print('Operation: ')
            operation = input()
            if operation == '+':
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    resultValue = (firstNumber + secondNumber)
                    print(resultValue)
                    exit()
            elif operation == '-':
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    resultValue = firstNumber - secondNumber
                    print(resultValue)
                    exit()
            elif operation == '*':
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    resultValue = firstNumber * secondNumber
                    print(resultValue)
                    exit()
            elif operation == '/':
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    resultValue = firstNumber / secondNumber
                    print(resultValue)
                    exit()
            elif operation == '%':
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    resultValue = firstNumber % secondNumber
                    print(resultValue)
                    exit()
            elif operation == '**':
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    resultValue = firstNumber ** secondNumber
                    print(resultValue)
                    exit()
            else:
                print('Operation not recognized')