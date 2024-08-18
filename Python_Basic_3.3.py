# Розділити один список на два списки

lst_of_numbers = []
result_list = []
first_list = []
second_list = []
index = len(lst_of_numbers) / 2

for i in range(len(lst_of_numbers)):
    if i < index:
        first_list.append(lst_of_numbers[i])
for i in range(len(lst_of_numbers)):
    if i > index:
        second_list.append(lst_of_numbers[i])

result_list.append(first_list)
result_list.append(second_list)
print(result_list)
