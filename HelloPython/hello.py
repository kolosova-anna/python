# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string("!", 5))
# print(new_string("!"))
# print(new_string(4))

# def concatenatio (* params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio("a", "s", "d", "w"))
# print(concatenatio("a", "1", "d", "2"))
#print(concatenatio(1,2,3,4))   #TypeError

# Рекурсия
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range (1,10):
#     list.append(fib(e))
# print(list)

# Кортежи
# (a) = (3, 4, 5)
# print(a)
# # print(a[0])
# print(a[-1])
#a[1] = 5  #НЕ Работает!!
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))

# Словари
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)
# print(dictionary['left'])

# dictionary['left'] = '⇐'
# print(dictionary['left'])
# del dictionary['left']

# for item in dictionary:  # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)

# q = a\
#     .union(b)\
#         .difference(a.intersection(b))
# print(a, b, c, u, i, dl, dr, q)

# s = frozenset(a)   №неизменяемое множество


# Списки
# list1 = [1,2,3,4,5]
# list2 = list1
# print(list1, list2)
# list1.pop()      #удаление последнего элемента
# print(list1)
# print(len(list1))
# list1.pop(2)      #удаление элемента с определенной позиции
# print(list1)
# list1.insert(2, 11)   #добавление элемента на позицию
# print(list1)
# list1.append(11)      #добавление элемента в конец
# print(list1)

