# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

data = [12, 'sadf', 5643]
print(data)
res = list(filter(lambda x: type(x) == int , data))
res2 = list(filter(lambda x: type(x) == str, data))
print(f'Числа: {res}')
print(f'Строки: {res2}')