"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
    Вывести каждое слово с новой строки.
        Строки необходимо пронумеровать.
            Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_string = input('Введите произвольную строку и несколких строк разделенную пробелом:\n')

user_line = user_string.split()

for num, line in enumerate(user_line):
    print(f'№ {num + 1} - {line[:10]}')
