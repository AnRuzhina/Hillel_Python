# Виведення числа в стовпчик

print("Enter your number")

number = input()
print(*number, sep='\n')

# or

print("Enter your number")

number = int(input())

number1 = number // 1000
print(number1)

number2 = number % 1000 // 100
print(number2)

number3 = number % 100 // 10
print(number3)

number4 = number % 10 // 1
print(number4)