# Создайте программу для игры в ""Крестики-нолики"".

# list = [["","",""], ["","",""], ["","","*"]]
# for i in range(9):
# if i % 2 == 0:
# print("1 игрок")
# Ввод: 3 2
# if i % 2 == 1:
# print("2 игрок")


from random import randint

print('#' * 10, 'Кристики-нолики', '#' * 10)
print()

field = list(range(1, 10))

def draw_field(field): #рисуем игровое поле
    print('-' * 13)
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-' * 13)

# draw_field(field)

def player_input(player): #ход игрока
    check = False
    while not check:
        player_one = input(f'Введитено номер поля для {player}: ')
        try:                #проверка на число
            player_one = int(player_one)
        except: 
            print('Введите целое число от 1 до 9')
            continue # если except  то 29 строчка
        if player_one >= 1 and player_one <= 9: # проверка не вышли ли за игровое поле
            if str(field[player_one - 1]) not in 'X0': #проверка на занятость ячейки в поле
                field[player_one - 1] = player
                check = True # если не занята, то ставим Х и выходим из функции
            else:
                print('Клетка занята. Повторите.') #если занята то повторяем цикл
        else:
            print('Введите число от 1 до 9') #если вышли за поле то повторяем цикл

def comp_input(player): #ход компа
    check = False
    while not check:
        player_two = randint(1,9)
        if str(field[player_two - 1]) not in 'X0':
            field[player_two - 1] = player
            check = True

def win_player(field): #проверка на совпадение в кортедже
    win_tuple = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for el in win_tuple:
        if field[el[0]] == field[el[1]] == field[el[2]]:
            return field[el[0]]
    return False

def master(field):
    count = 0
    win = False
    while not win:
        draw_field(field)
        if count % 2 == 0:
            player_input('X')
        else:
            print('Ход компа:')
            comp_input('0')
        count += 1
        if count > 4:
            temp = win_player(field)
            if temp:
                print(f'{temp}, ВЫИГРАЛ!')
                win = True
                break
        if count == 9:
            print('Ничья!')
            break
    draw_field(field)
master(field)

