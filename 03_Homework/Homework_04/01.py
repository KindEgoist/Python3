# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

# Вычислить число PI c заданной точностью d

from math import pi


def input_number():
    while True:
        try:
            num = int(input('Введите число: '))
            return num
        except:
            print('Ошибка ввода, попробуйте еще раз')
          
def fix(pi: float, n=0):
    a, b = str(pi).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

# num = input_number()
# print(fix(pi, num)) 

# import math
# num = int(input('Введите число N: '))
# num = num + 2
# pi = str(math.pi)[0:num]
# print(float(pi))


 
