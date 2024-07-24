# Перемістити елемент у списку

list1 = []
if len(list1) / 2 != 0 and len(list1) != 1 and len(list1) != 3 and len(list1) != 5 and len(list1) / 4 != 0:
    list1.remove(10)
    list1.insert(0, 10)
    print(list1)

if len(list1) / 2 != 0 and len(list1) == 1 and len(list1) != 3 and len(list1) != 5:
    print(list1)

if len(list1) / 2 == 0 and len(list1) != 1 and len(list1) != 3 and len(list1) != 5:
    print(list1)

if len(list1) / 2 != 0 and len(list1) != 1 and len(list1) == 5 and not len(list1) / 4 == 0:
    list1.remove(8)
    list1.insert(0, 8)
    print(list1)
