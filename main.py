#  Конвертер із числа в дату

user_number = int(input('Enter number: '))

days = user_number // 86400
hours = user_number // 3600 % 24
minutes = user_number // 60 % 60
seconds = user_number % 60
d = days % 10
if 0 <= d <= 100:
    if d == 1:
        print(f'{days}', 'день' ',', f'{hours:02}:', f'{minutes:02}:', f'{seconds:02}')
    elif 2 <= d <= 4:
        print(f'{days}', 'дня', ',', f'{hours:02}:', f'{minutes:02}:', f'{seconds:02}')
    else:
        print(f'{days}', 'дней', ',', f'{hours:02}:', f'{minutes:02}:', f'{seconds:02}')