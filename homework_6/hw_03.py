# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

from itertools import groupby

def names_dict (list_1):
    if "" not in list_1:
        dictionary = {ch: list(i) for ch, i in groupby(sorted(list_1), key = lambda i: i[0]) if ch}
        return (dictionary)
    return 'Error'

my_list = input('Введите имена через пробел: ').split()
print (my_list)
print(names_dict(my_list))