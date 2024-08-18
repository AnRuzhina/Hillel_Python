# Перемістити всі нулі до кінця списку

list1 = [0, 0, 2, 1, 3, 0, 0, 3]
if list1 != [0]:
    list1 = [i for i in list1 if i != 0]
    list1.extend([0] * len(list1))
    print(list1)
else:
    list1 = [0]
    print(list1)
