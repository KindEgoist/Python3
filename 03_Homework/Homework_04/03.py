# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# 3 1 2 3
# 2 1

def input_number():
    list = []
    while True:
        try:
            size = int(input("Введите длину массива: "))
            for i in range(size):
                list.append(int(input(f"Введите число {i + 1}: ")))
            return list
        except:
            print('Ошибка ввода, попробуйте еще раз')

def non_repeating_list(list):
    my_list = []
    for i in list:
        if list.count(i) < 2:
            my_list.append(i)
    return my_list       

my_list = input_number()

print(f'Список: {my_list}')
print(f"Список из неповторяющихся элементов: {non_repeating_list(my_list)}")

# number = [1, 2, 3, 3, 4, 5, 5, 2]
# result = []
# for i in number:
#     if number.count(i) < 2:
#         result.append(i)
# print(result) #1 4