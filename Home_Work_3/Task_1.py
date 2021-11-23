"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divis_two_numbers(a, b):
    try:
        div = a / b
    except ValueError:
        return "Введите цифры"
    except ZeroDivisionError:
        return "Неправельный делитель! На ноль делить нельзя"
    return div


a = float(input('Введите делимое число: '))
b = float(input('Введите делитель числа: '))
print(divis_two_numbers(a, b))
