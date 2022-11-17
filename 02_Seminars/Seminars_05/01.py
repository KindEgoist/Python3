# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: 1 2 3 5 6 7
# Вывод: 4

# with open ('sem5.txt','r') as file:
#     # print(file.readline())
#     spisok = list(map(int, (file.readline().split())))
#     print(spisok)
#     for i in range(1, len(spisok)):
#         if spisok[i] - 1 != spisok[i - 1]:
#             print(spisok[i] - 1)


def find_lost_number(spisok):
    for i in range(1, len(spisok)):
        if spisok[i] - 1 != spisok [i - 1]:
            return spisok[i] - 1
with open ('sem5.txt','r') as file:
    spisok = [int(i) for i in file.readline().split()]
    print(find_lost_number(spisok))