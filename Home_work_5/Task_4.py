# -*- coding: utf-8 -*-
"""
Создать (не программно) текстовый файл со следующим содержимым:
                        One — 1
                        Two — 2
                        Three — 3
                        Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def rewrite_file():
    decoder = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    with open('Text_For_Task_4.txt', encoding="utf-8") as f_obj_r:
        with open('Text_For_Task_4_r.txt', 'w', encoding="utf-8") as f_obj_w:
            my_list = f_obj_r.readlines()
            for i in my_list:
                i = i.split(' ', 1)
                new_text.append(decoder[i[0]] + ' ' + i[1])
            f_obj_w.writelines(new_text)


rewrite_file()
