# Разделить один список на два списка
# [1, 2, 3, 4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5], [1], []

lst_of_numbers = [1]

if len(lst_of_numbers) / 2 != 0 and len(lst_of_numbers) != 1 and len(lst_of_numbers) != 3:
    lst_multiple = [lst_of_numbers[i:i + 3] for i in range(0, len(lst_of_numbers), 3)]
    print(lst_multiple)

elif not len(lst_of_numbers) / 2 == 0 and len(lst_of_numbers) != 1:
    lst_multiple = [lst_of_numbers[i:i + 2] for i in range(0, len(lst_of_numbers), 2)]
    print(lst_multiple)

elif len(lst_of_numbers) != 0:
    lst_multiple = [lst_of_numbers[i:i + 1] for i in range(0, len(lst_of_numbers), 1)]
    lst_multiple.append([])
    print(lst_multiple)

elif len(lst_of_numbers) == 0:
    lst_multiple = [lst_of_numbers[i:i + 1] for i in range(0, len(lst_of_numbers), 1)]
    lst_multiple.append([])
    lst_multiple.append([])
    print(lst_multiple)
