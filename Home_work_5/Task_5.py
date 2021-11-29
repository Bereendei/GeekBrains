"""
Создать (программно) текстовый файл,
    записать в него программно набор чисел,
        разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

try:
    with open("Text_For_Task_5.txt", "w+", encoding="utf-8") as f_obj:
        numbers = input('Введите числа через пробел: ')
        f_obj.writelines(numbers)
        new_numb = numbers.split()
        print(sum(map(int, new_numb)))
except IOError:
    print('Ошибка файла')
except ValueError:
    print('Ошибка ввода данных')

# with open('xxx.txt', 'w+') as file:
#     nums_str = file.read().split()
#     sum = 0
#     for num in nums_str:
#         sum += int(num)
# print(sum)
