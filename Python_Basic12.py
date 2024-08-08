# Ім'я змінної
import string
import keyword

user_string = input("Enter your nick(can't start with number/be reg.name /include cap.letter,punctuation(only one _ : ")
donut_1 = True
for character in user_string:
    donut_1 = (character not in string.punctuation or character == '_') and not character == ' '
    if not donut_1:
        break
number_t = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
donut = not user_string.startswith(number_t, 0, 9)
donut_2 = '__' not in user_string
donut_3 = user_string.lower() == user_string
donut_4 = True
for keyword_1 in keyword.kwlist:
    if keyword_1 == user_string:
        donut_4 = False
        break
print(donut and donut_1 and donut_2 and donut_3 and donut_4)
