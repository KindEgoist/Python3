# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11


# data = input('Введите число: ')
# spisok = list(filter(lambda x: x.isdigit(), data))
# spisok = [int(item) for item in spisok]
# print(sum(spisok))

# data = float(input('Введите вещественное число: '))
# data = str(data)
# spisok = list(filter(lambda x: x.isdigit(), data))
# spisok = [int(item) for item in spisok]
# print(sum(spisok))

data = input('Введите вещественное число: ')
summa = sum(map(int, data.replace('.','').replace('-','')))
print(summa)