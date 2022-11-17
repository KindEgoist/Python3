import imp
tuple_data = ('Фамилия', 'Имя', 'Телефон', 'Описание')

def convert_lst(spisok):
    array = []
    x = int(len(spisok)/4)
    y = 1
    for r in range(x):
        dic_data = {}
        for i in range(len(tuple_data)):
            dic_data[tuple_data[i]] = spisok [i]
        array.append(dic_data)
        del spisok [:4]
    return array

def poisk():
    spisok = imp.impor2()
    array = convert_lst(spisok)
    fin = input('Введите Фамилию или Имя с заглавной буквы или телефон: ') 
    for el in array:
        for v in el.values():
            if v == fin:
                print (f'Результат поиска: {el}')


    
