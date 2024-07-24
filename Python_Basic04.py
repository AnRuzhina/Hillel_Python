# Розділити один список на два списки
# Я для вашої зручності продублювала умову для кожного рішення, щоб результат одразу по всім було видно:)

lst_of_numbers = [1, 2, 3, 4, 5, 6]

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

lst_of_numbers1 = [1, 2, 3]

if len(lst_of_numbers1) / 2 != 0 and len(lst_of_numbers1) != 1 and len(lst_of_numbers1) != 3:
    lst_multiple1 = [lst_of_numbers1[i:i + 3] for i in range(0, len(lst_of_numbers1), 3)]
    print(lst_multiple1)

elif not len(lst_of_numbers1) / 2 == 0 and len(lst_of_numbers1) != 1:
    lst_multiple1 = [lst_of_numbers1[i:i + 2] for i in range(0, len(lst_of_numbers1), 2)]
    print(lst_multiple1)

elif len(lst_of_numbers1) != 0:
    lst_multiple1 = [lst_of_numbers1[i:i + 1] for i in range(0, len(lst_of_numbers1), 1)]
    lst_multiple1.append([])
    print(lst_multiple1)

elif len(lst_of_numbers1) == 0:
    lst_multiple1 = [lst_of_numbers1[i:i + 1] for i in range(0, len(lst_of_numbers1), 1)]
    lst_multiple1.append([])
    lst_multiple1.append([])
    print(lst_multiple1)

lst_of_numbers2 = [1, 2, 3, 4, 5]

if len(lst_of_numbers2) / 2 != 0 and len(lst_of_numbers2) != 1 and len(lst_of_numbers2) != 3:
    lst_multiple2 = [lst_of_numbers2[i:i + 3] for i in range(0, len(lst_of_numbers2), 3)]
    print(lst_multiple2)

elif not len(lst_of_numbers2) / 2 == 0 and len(lst_of_numbers2) != 1:
    lst_multiple2 = [lst_of_numbers2[i:i + 2] for i in range(0, len(lst_of_numbers2), 2)]
    print(lst_multiple2)

elif len(lst_of_numbers2) != 0:
    lst_multiple2 = [lst_of_numbers2[i:i + 1] for i in range(0, len(lst_of_numbers2), 1)]
    lst_multiple2.append([])
    print(lst_multiple2)

elif len(lst_of_numbers2) == 0:
    lst_multiple2 = [lst_of_numbers2[i:i + 1] for i in range(0, len(lst_of_numbers2), 1)]
    lst_multiple2.append([])
    lst_multiple2.append([])
    print(lst_multiple2)

lst_of_numbers3 = [1]

if len(lst_of_numbers3) / 2 != 0 and len(lst_of_numbers3) != 1 and len(lst_of_numbers3) != 3:
    lst_multiple3 = [lst_of_numbers3[i:i + 3] for i in range(0, len(lst_of_numbers3), 3)]
    print(lst_multiple3)

elif not len(lst_of_numbers3) / 2 == 0 and len(lst_of_numbers3) != 1:
    lst_multiple3 = [lst_of_numbers3[i:i + 2] for i in range(0, len(lst_of_numbers3), 2)]
    print(lst_multiple3)

elif len(lst_of_numbers3) != 0:
    lst_multiple3 = [lst_of_numbers3[i:i + 1] for i in range(0, len(lst_of_numbers3), 1)]
    lst_multiple3.append([])
    print(lst_multiple3)

elif len(lst_of_numbers3) == 0:
    lst_multiple3 = [lst_of_numbers3[i:i + 1] for i in range(0, len(lst_of_numbers3), 1)]
    lst_multiple3.append([])
    lst_multiple3.append([])
    print(lst_multiple3)

lst_of_numbers4 = []

if len(lst_of_numbers4) / 2 != 0 and len(lst_of_numbers4) != 1 and len(lst_of_numbers4) != 3:
    lst_multiple4 = [lst_of_numbers4[i:i + 3] for i in range(0, len(lst_of_numbers4), 3)]
    print(lst_multiple4)

elif not len(lst_of_numbers4) / 2 == 0 and len(lst_of_numbers4) != 1:
    lst_multiple4 = [lst_of_numbers4[i:i + 2] for i in range(0, len(lst_of_numbers4), 2)]
    print(lst_multiple4)

elif len(lst_of_numbers4) != 0:
    lst_multiple4 = [lst_of_numbers4[i:i + 1] for i in range(0, len(lst_of_numbers4), 1)]
    lst_multiple4.append([])
    print(lst_multiple4)

elif len(lst_of_numbers4) == 0:
    lst_multiple4 = [lst_of_numbers4[i:i + 1] for i in range(0, len(lst_of_numbers4), 1)]
    lst_multiple4.append([])
    lst_multiple4.append([])
    print(lst_multiple4)

