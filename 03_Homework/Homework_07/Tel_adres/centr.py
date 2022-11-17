import input_and_output, exp, imp, fine

def button_click():
    print('Экспорт данных')
    print('Введите yes если хотите продолжить')
    print('Введите no если хотите закончить')
    flag = input()
    while flag == 'yes':
        data = input_and_output.vvod()
        input_and_output.vivod(data)
        exp.log(data)
        print('Введите yes если хотите продолжить')
        print('Введите no если хотите закончить')
        flag = input()
    print('Импортировать данные?\nyes если согласны.\n no если выйти')
    flag = input()
    if flag == 'yes':
        imp.impor()
        print('Сделать поиск?\nyes если согласны.\n no если выйти')
        flag = input()
        if flag == 'yes':
            fine.poisk()
        else:
            print('Программа завершина')
    elif flag == 'no':
        print('Программа завершина')

            

       