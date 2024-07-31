list1 = [1,3,4]
i = 0
list2 = [i for i in list1 if i != 0]
zeros = len(list1) - len(list2)
list2.extend([0] * zeros)
print(list2)
