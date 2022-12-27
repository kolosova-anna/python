# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import *

num = Decimal(input('Enter a real number: '))
accuracy = Decimal(input('Enter the required accuracy: '))
new_num = Decimal(num).quantize(Decimal(accuracy), rounding = ROUND_DOWN)
print (new_num)