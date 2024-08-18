# Перемістити елемент у списку

list1 = [1, 2, 3, 5]
if len(list1) != 0:
    list1.insert(0, list1[-1])
    del list1[-1]
    print(list1)

if len(list1) == 0:
    print(list1)
