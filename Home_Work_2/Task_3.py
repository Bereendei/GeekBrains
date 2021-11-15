"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}

while True:
    user_month = int(input('Введите номер месяц: '))
    if user_month > 12 or user_month < 1:
        print('Некорректное число месяца')
        continue
    else:
        break
if user_month == 12 or user_month == 1 or user_month == 2: print(seasons_list[0], list), print(seasons_dict[0], dict)
if user_month == 3 or user_month == 4 or user_month == 5: print(seasons_list[1], list), print(seasons_dict[1], dict)
if user_month == 6 or user_month == 7 or user_month == 8: print(seasons_list[2], list), print(seasons_dict[2], dict)
if user_month == 9 or user_month == 10 or user_month == 11: print(seasons_list[3], list), print(seasons_dict[3], dict)
