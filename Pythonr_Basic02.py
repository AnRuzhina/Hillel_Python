# Необхідно "перевернути" 5-ти значне число

number = int(input('Enter your number: '))

number5 = number % 10 // 1
print(number5, end='')

number4 = number % 100 // 10
print(number4, end='')

number3 = number % 1000 // 100
print(number3, end='')

number2 = number % 10000 // 1000
print(number2, end='')

number1 = number // 10000
print(number1, end='')





