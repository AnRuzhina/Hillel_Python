# Перевірити чи є парним чи ні

def is_even(digit):
    return digit % 2 == 0


result = is_even(digit=int(input()))
print(result)

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
