# Додати 1 до числа

def add_one(some_list):
    list_str = ''.join(map(str, some_list))
    number = int(list_str)
    number += 1

    return list(map(int, str(number)))


user_input = input('')
input_list = list(map(int, user_input.split()))

result = add_one(input_list)
print(result)

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
