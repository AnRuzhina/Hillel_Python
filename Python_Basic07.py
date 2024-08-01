list1 = [1, 0, 3, 0, 4]
list1 = [i for i in list1 if i != 0]
zeros = len(list1)
list1.extend([0] * zeros)
list1.remove(0)
print(list1)
