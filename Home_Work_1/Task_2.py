"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
user_time = int(input('Введите время в секундах: '))

hour = user_time // 3600
minutes = (user_time - hour * 3600) // 60
second = user_time - (hour * 3600 + minutes * 60)

if hour < 24:
    print(f'Время в формате чч:мм:сс  {hour:02}:{minutes:02}:{second:02}')
elif (hour > 24) and (hour < 7300):
    day = hour // 24
    print(f'Кажется нужно добавить дни  {day:02}:{hour:02}:{minutes:02}:{second:02}')
else:
    print('Ох, походу тут еще и месяца, а то и года... Мне лень! Cам считай!')
