#  Конвертер із числа в дату

user_number = int(input('Enter number: '))

days = user_number // 86400
hours = user_number // 3600 % 24
minutes = user_number // 60 % 60
seconds = user_number % 60

# Визначення правильної форми слова "день"
d = days % 10
if 11 <= days % 100 <= 14:
    day_word = "днів"
elif d == 1:
    day_word = "день"
elif 2 <= d <= 4:
    day_word = "дні"
else:
    day_word = "днів"

# Формування та виведення результату
print(f'{days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}')
