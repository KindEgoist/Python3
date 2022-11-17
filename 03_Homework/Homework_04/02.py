# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

def input_number():  
    while True:
        try:
            num = int(input("Введите число N: "))
            return num
        except:
            print('Ошибка ввода, попробуйте еще раз')


def simple_multipliers(num):
   i = 2
   list = []
   while i * i <= num:
       while num % i == 0:
           list.append(i)
           num = num / i
       i += 1
   if num > 1:
       list.append(int(num))
   return list
            

print(simple_multipliers(input_number()))

# num = int(input('Введите N: '))
# spisok = []
# i = 2
# while i <= num:
#     if num % i == 0:
#         spisok.append(i)
#         num //= i
#     else:
#         i += 1
# print(spisok)