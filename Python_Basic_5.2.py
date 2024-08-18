#  Модифікувати калькулятор

while True:
    question = input("Make calculation? (y/n): ").strip().lower()

    if question == "y":
        numb1 = float(input('Enter first number: '))
        operator = input('Enter operator ( +, -, *, /): ')
        numb2 = float(input('Enter second number: '))

        if operator == "+":
            result = numb1 + numb2
        elif operator == "-":
            result = numb1 - numb2
        elif operator == "*":
            result = numb1 * numb2
        elif operator == "/":
            if numb2 == 0:
                print('Mistake: division by zero!')
                continue  # Повертаємося на початок циклу
            result = numb1 / numb2
        else:
            print("Mistake: invalid operator")
            continue  # Повертаємося на початок циклу

        print("Result:", result)
    elif question == "n":
        print("Calculation finished")
        break  # Виходимо з циклу
    else:
        print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
