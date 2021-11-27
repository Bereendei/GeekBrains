"""
Создать текстовый файл (не программно),
    сохранить в нем несколько строк,
        выполнить подсчет количества строк,
            количества слов в каждой строке.
"""

with open("Text_For_Task_2.txt") as f_obj:
    num = 1
    for num, i in enumerate(f_obj):
        print(f'Строка № {num + 1} кол-во символов {len(i)}')
        num += num

f_obj = open('Text_For_Task_2.txt')
content = f_obj.read()
content = content.split()
print(f'Всего символов в файле {len(content)}')
f_obj.close()
