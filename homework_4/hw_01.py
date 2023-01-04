# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import *

num = Decimal(input('Enter a real number: '))
def decimal_number(n):
    accuracy = Decimal(input('Enter the required accuracy: '))
    new_num = Decimal(num).quantize(Decimal(accuracy), rounding = ROUND_HALF_EVEN)
    return new_num

dec_num = decimal_number (num)
print (dec_num)