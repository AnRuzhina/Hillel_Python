#  Добуток чисел
def multiply_digits_until_single_digit(number):
    while number > 9:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product
    return number


user_input = int(input("Enter number: "))
result = multiply_digits_until_single_digit(user_input)
print(f"Result: {result}")
