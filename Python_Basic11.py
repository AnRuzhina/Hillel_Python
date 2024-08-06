#  Модифікувати калькулятор

question = input("Make calculation?: ")
while question in question:
    answer = question
    if answer == "y":
        numb1 = float(input('Enter first number:  '))
        operator = input('Enter operator ( +, -, *, /): ')
        numb2 = float(input('Enter second number:  '))
        if operator == "+":
            result = numb1 + numb2
        elif operator == "-":
            result = numb1 - numb2
        elif operator == "*":
            result = numb1 * numb2
        elif operator == "/":
            if numb2 == 0:
                print('Mistake: division by zero!')
                exit()
            result = numb1 / numb2
        else:
            print("Mistake: invalid operator")
            exit()
        print("Result:", result)
        question = input("Make calculation?: ")
        continue
    if answer == "n":
        print("Calculation finished")
    break
