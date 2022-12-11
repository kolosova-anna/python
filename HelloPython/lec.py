# print('hello world')
# value =None
# print(type(value))

a = 123
b = 1.23
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# value = 12334
# print(type(value))
# print(value)

s = 'hello world'
# s = 'hello "world"'
# s = 'hello \nworld'
# print(s)  вывод строки

# print(a, '-',b, '-',s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = [1,2,3]  #лист(массив) чисел
# list = ['1', 'a', 'hello'] #лист строк
# col = ['hello', 1,2,3.5, True]
# print(list)
# print(col)

# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a, '+' , b, '=', a+b)

# a = +3  #унарный плюс
# b = -4  #унарный минус (инверсия)
# c=a+b
# c=a/b
# c=a//b  #целочисленное деление
# c = a % b  #остаток от деления
# c = b ** a  #возведение в степень

# a =1.3123
# b = 3
# c = round(a * b, 5)
# print(c)

# a = 3
# a +=5
# print(a)


# a = 1 < 3 and 5 > 2
# print(a)

# a = 'hello'
# b = 'hello'

# a = [1,2]
# b = [1,2]
# print(a==b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func < T > x)

# f = 1 > 2 or 4 < 6
# f = [1,2,3,4]
# print(f)
# print(2 in f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b= int(input('b = '))5
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == "марина":
#     print('Я так ждала вас, Марина!')
# elif username == "Ильнар":
#     print('Ильнар - топ!')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in 'qwe-rty':
#     print(i)

# text = 'съешь еще этих мягких французских булок'

# print(len(text))            #39
# print('еще' in text)        #True
# print(text.isdigit())       #False
# print(text.islower())       #True
# print(text.replace('еще','ЕЩЕ'))

# print(text[0])              #с
# print(text[len(text) - 1])  #к
# print(text[-1])             #к
# print(text[:5])             #съешь


# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1, 6)
# numbers = list(ran)
# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)


# colors = ['red', 'green', 'blue']
# for e in colors:
#      print(e)  # red green blue

# for e in colors:
#      print(e*2)  # redred greengreen blueblue

# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


def f(x):
    return x**2


