# Діапазон букв

import string
from _pyrepl.commands import end

letters = input("Enter 2 letters separated by a hyphen: ")
dict_1 = string.ascii_letters
alfabet = dict_1
first_letter = letters[0]
second_letter = letters[2]
fist_letter_index = dict_1.index(first_letter)
second_letter_index = dict_1.index(second_letter)
print(alfabet[fist_letter_index: second_letter_index + 1])
