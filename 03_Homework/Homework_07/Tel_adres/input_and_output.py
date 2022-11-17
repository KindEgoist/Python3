tuple_data = ('Фамилия', 'Имя', 'Телефон', 'Описание')

def vvod():
    dict_data = {}
    for el in tuple_data:
        temp = input(f'Введите {el}: ')
        dict_data[el] = temp
    return dict_data

def vivod(dict_data):
    stroka = ""
    for k, v in dict_data.items():
        stroka += str(k) + ': ' + str(v) + ', '
    stroka = stroka[:-2] + ';'
    print(f'Полученные данные: {stroka}')

def vivod_imp(spisok):
        x = int(len(spisok)/4)
        y = 1
        for r in range(x):
            dic_data = {}
            for i in range(len(tuple_data)):
                dic_data[tuple_data[i]] = spisok [i]
            stroka = ""
            for k, v in dic_data.items():
                stroka += str(k) + ': ' + str(v) + ', '
            stroka = stroka[:-2] + ';'
            print(f'{y}: {stroka}')
            y += 1     
            del spisok [:4]

