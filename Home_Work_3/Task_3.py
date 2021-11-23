"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func():
    user_input = input('Введите 3 аргумента через пробел: ')
    input_list = sorted(user_input.split())
    k = (int(input_list[-1]) + int(input_list[-2]))
    return print(k)


c = my_func()
