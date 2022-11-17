# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности. Без использования count()
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

def find_unique(data):
    result = []
    result_new = []
    for el in data:
        if el not in result and el not in result_new:
            result.append(el)
            result_new.append(el)
        elif el in result:
            result.remove(el)
    return sorted(result)

sequence = [1, 2, 3, 5, 1, 5, 1, 3, 10, 1, 7, 5, 4, 5, 1, 9, 9, 9]
print(sequence)
print(find_unique(sequence))
