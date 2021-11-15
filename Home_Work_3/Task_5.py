"""
 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
 Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел,
    то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def user_sum():
    sum_list = 0
    ex = False
    while ex == False:
        input_user = input('Введите числа через пробел или "ex" для завершения: ')
        input_list = input_user.split()
        res = 0
        for i in input_list:
            if i == 'ex':
                ex = True
                break
            else:
                res += int(i)
        sum_list = sum_list + res
        print(f'Текущая сумма: {sum_list}')


user_sum()
