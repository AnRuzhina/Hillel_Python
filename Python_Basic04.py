# Розділити один список на два списки


lst_of_numbers = []

if len(lst_of_numbers) / 2 != 0 and len(lst_of_numbers) != 1 and len(lst_of_numbers) != 3:
    lst_multiple = [lst_of_numbers[i:i + 3] for i in range(0, len(lst_of_numbers), 3)]
    print(lst_multiple)

elif not len(lst_of_numbers) / 2 == 0 and len(lst_of_numbers) != 1:
    lst_multiple1 = [lst_of_numbers[i:i + 2] for i in range(0, len(lst_of_numbers), 2)]
    print(lst_multiple1)

elif len(lst_of_numbers) != 0:
    lst_multiple2 = [lst_of_numbers[i:i + 1] for i in range(0, len(lst_of_numbers), 1)]
    lst_multiple2.append([])
    print(lst_multiple2)

elif len(lst_of_numbers) == 0:
    lst_multiple3 = [lst_of_numbers[i:i + 1] for i in range(0, len(lst_of_numbers), 1)]
    lst_multiple3.append([])
    lst_multiple3.append([])
    print(lst_multiple3)
