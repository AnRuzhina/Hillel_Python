# Розділити один список на два списки

lst_of_numbers = []

if len(lst_of_numbers) != 0 and len(lst_of_numbers) != 1 and len(lst_of_numbers) != 2:
    lst_multiple = [lst_of_numbers[i:i + 3] for i in range(0, len(lst_of_numbers), 3)]
    print(lst_multiple)

if len(lst_of_numbers) != 0 and len(lst_of_numbers) != 1 and len(lst_of_numbers) == 2:
    lst_multiple = [lst_of_numbers[i:i + 1] for i in range(0, len(lst_of_numbers), 1)]
    print(lst_multiple)

elif len(lst_of_numbers) != 0 and len(lst_of_numbers) == 1:
    lst_multiple = [lst_of_numbers[i:i + 1] for i in range(0, len(lst_of_numbers), 1)]
    lst_multiple.append([])
    print(lst_multiple)

elif len(lst_of_numbers) == 0:
    lst_multiple = [lst_of_numbers[i:i + 1] for i in range(0, len(lst_of_numbers), 1)]
    lst_multiple.append([])
    lst_multiple.append([])
    print(lst_multiple)
