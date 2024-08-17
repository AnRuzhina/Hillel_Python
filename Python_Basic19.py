# Пошук спільних елементів


def common_elements():
    multiples_of_3 = {y for y in range(100) if y % 3 == 0}
    multiples_of_5 = {y for y in range(100) if y % 5 == 0}
    intersection = multiples_of_3 & multiples_of_5

    return intersection


result = common_elements()
print(result)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test1'
print('ОК')
