"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
        имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def form_users():
    name = input('Имя: ')
    surname = input('Фамилия: ')
    year = input('Дата рождения: ')
    city = input('Город проживания: ')
    email = input('email: ')
    phone_number = input('Номер телефона')
    return print(' '.join([name, surname, year, city, email, phone_number]))


a = form_users()


# Не до конца понял задание, надеюсь хоть один вариант правильный

def my_func(**kwargs):
    return kwargs


print(my_func(name='Ivan', surname='Sidorov', year='96', city='Rostov-on-Don', email='error@mail.ru',
              phone_number='8-888-888-88-88'))
