# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф
# a) Добавьте игру против бота
# *** b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

from random import randint


def player_input():
    check = False
    while not check:
        player_one = input(f'Введите число от 1 до 28: ')
        try:               
            player_one = int(player_one)
        except: 
            print('Введите целое число от 1 до 28')
            continue 
        if player_one >= 1 and player_one <= 28: 
            return player_one
        else:
            print('Введите число от 1 до 28') 

def master():
    x = 2021
    while x != 0:
        if x <= 28:
            print('Заберите оставшиеся конфеты. И вы Выиграли!')
            break
        n1 = player_input()
        x = x - n1
        print (f'Осталось конфет: {x}')
        if x <= 28:
            print('Комп забрал последние конфеты. И он Выиграл!')
            break
        n2 = randint(1, 28)
        x = x - n2
        print(f'Комп взял конфет {n2}. Осталось: {x}')
    
master()


