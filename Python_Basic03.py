# Виведення числа в стовпчик

number = input('Enter your number: ')
print(*number, sep='\n')

# or

number = int(input("Enter your number:  "))

number1 = number // 1000
print(number1)

number2 = number % 1000 // 100
print(number2)

number3 = number % 100 // 10
print(number3)

number4 = number % 10 // 1
print(number4)