"""
Узнайте у пользователя число n.
    Найдите сумму чисел n + nn + nnn.
        Например, пользователь ввёл число 3.
            Считаем 3 + 33 + 333 = 369.
"""

user_number = input('Введи любую цифру: ')

b = user_number + user_number
c = user_number + user_number + user_number

print(f'Как то так {user_number} + {b} + {c} = {int(user_number) + int(b) + int(c)}')
