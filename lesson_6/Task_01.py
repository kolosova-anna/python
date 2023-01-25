# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,* приоритет операций стандартный.
# * Добавьте скобки, приоритет операций меняется.

exp = "4 * 3 - 1 / 9 - 7 * -1".split()
actions = {
"^": lambda x, y: str(float(x) ** float(y)),
"*": lambda x, y: str(float(x) * float(y)),
"/": lambda x, y: str(float(x) / float(y)),
"+": lambda x, y: str(float(x) + float(y)),
"-": lambda x, y: str(float(x) - float(y))
}

exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()

def calculator(new_lst):

    for i, val in enumerate(new_lst):
        if isinstance(val, list):
            new_lst[i] = calculator(val)

    index_lst = [i for i, val in enumerate(new_lst) if val in "*/"]

    while index_lst:
        index_op = index_lst[0]
        a, b, c = new_lst[index_op - 1: index_op + 2]
        new_lst.insert(index_op - 1, actions[b](a, c))
        del new_lst[index_op: index_op + 3]
        index_lst = [i for i, val in enumerate(new_lst) if val in "*/"]

    while len(new_lst) > 1:
        a, b, c = new_lst[:3]
        del new_lst[:3]
        new_lst.insert(0, actions[b](a, c))

    return new_lst[0]

def cut(ls):
    lst = []
    index_ = 0

    while index_ < len(ls):
        if ls[index_] == "(":
            end = ls.index(")")
            lst.append(ls[index_ + 1: end])
            index_ = end
        else:
            lst.append(ls[index_])
        index_ += 1
    return lst

user_ls = input("...").split()
print(calculator(cut(user_ls)))





# Проверка комплексных чисел:
# 1. Нельзя использовать //, %
# 2. Нельзя пользоваться функцией sqrt

# n = input('Enter 1 real part: ')
# m = input('Enter 1 imaginary number: ')

# n1 = input('Enter 2 real part: ')
# m1 = input('Enter 2 imaginary number: ')


# complex(n, m)
# complex (n1, m1)

# Проверка ввода комплексного числа
# При вводе каждой части комплексных чисел делаем проверку

# def check_complex_part1 (a = input('Enter real part: ')):
#         if a.isdigit():
#             return int(a)
#         else:
#             print ('Error')
#             a = input('Enter once again: ')

# def check_complex_part2 (b = input('Enter imaginary number: ')):
#         if b.isdigit():
#             return int(b)
#         else:
#             print ('Error')
#             b = input('Enter once again: ')

# num = complex (n(check_complex_part1(n), m(check_complex_part2(m))))
# num = complex (n, m)
# print (num)



def check_complex1():
    n = input('Enter real part: ')
    if n.isdigit():
        n = int(n)
        return n
    else:
        print ('Error')
        n = check_complex1()


def check_complex2():
    m = input('Enter imaginary number: ')
    if m.isdigit():
        m = int(m)
        return m
    else:
        print ('Error')
        m = check_complex2()

# n = input('Enter real part: ')
a = check_complex1()
# m = input('Enter imaginary number: ')
b = check_complex2()
num = complex (a, b)
print (num)