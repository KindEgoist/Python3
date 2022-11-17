# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# stroka = "aaabbbbccbbb"
# stroka = "3a4b2c3b"
# Входные данные хранятся в отдельных текстовых файлах.

def sjatie(): # тут при использование списка и перебор по индексам
    with open('h5_3_1.txt', 'r') as file:
        res = file.readline()
        print(f'В файле: {res}')
    list = []
    count = 1
    for i in range(len(res)-1):
        if res[i] == res[i + 1]:
            count += 1
        else:
            string = str(count) + res[i]
            list.append(string)
            count = 1
    string = str(count) + res[i]
    list.append(string)
    resalt = ''.join(list)
    print(f'Результат: {resalt}')

def raspokovka(): # тут при использование строк и перебор по елементам. Для разнообразия сделал :)) а вообще можно так и так каждую функцию
    with open('h5_3_2.txt', 'r') as file:
        res = file.readline()
        print(f'В файле: {res}')
    chislo = ""
    decode = ""
    for e in res:
        if  e.isdigit():
            chislo += e
        else:
            decode += e * int(chislo)
            chislo = ""
    print(f'Результат: {decode}')   

def master():
    print('Сжатие или Распоковка?')
    print('s - сжатие')
    print('r - распоковка')
    check = False
    while not check:
        v = (input('Что делаем?: '))
        
        if v == 's' or v == 'r':
            if v == 's':
                sjatie()
                break 
            else:
                raspokovka()
                break
        else:
            print('Не то ввели. Повторите! s - сжатие или r - распоковка')


master()

