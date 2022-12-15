# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

def distance():
    x1 = int(input('Введите x1: '))
    y1 = int(input('Введите y1: '))
    x2 = int(input('Введите x2: '))
    y2 = int(input('Введите y2: '))
    num = int((x2 - x1)**2 + (y2 - y1)**2)
    import math
    dist = round(float(math.sqrt(num)), 3)
    print(dist)

distance()