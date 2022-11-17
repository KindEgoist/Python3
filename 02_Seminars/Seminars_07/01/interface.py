import digit, input_view, logir

def button_click():
    print('Введите 0 если хотите продолжить')
    print('Введите 1 если хотите закончить')
    flag = int(input())
    while flag == 0:
        primer = digit.parse()
        result = digit.calc(primer)
        input_view.view_data(result)
        logir.log(primer, result)
        print('Введите 0 если хотите продолжить')
        print('Введите 1 если хотите закончить')
        flag = int(input())
    print('Программа кончилась')