"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import cycle

def my_count(user_start_number, user_stop_number):
    for el in count(user_start_number):
        if el > user_stop_number:
            break
        else:
            print(el)


def my_cycle(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_count(user_start_number=int(input("Введите начальное число: ")), user_stop_number=int(input("Введите конечное число: ")))
my_cycle(my_list=["text_one", 2], iteration=int(input("enter iteration: ")))
