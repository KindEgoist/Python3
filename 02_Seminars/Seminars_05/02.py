# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# with open ('sem5_2.txt','r') as file:
#     # print(file.readline())
#     spisok = list(file.readline().split())
#     print(spisok)
#     stop_list = 'абв'
#     filter_list = ' '.join(filter(lambda x: stop_list not in x, spisok))
#     print(filter_list)

# substr = 'абв'

# with open('sem5_2.txt', 'r') as file:
#     for word in file.read().split():
#         if word.find(substr) == -1:
#           print(word, end=' ')

with open('sem5_2.txt', 'r') as file:
    res = file.readline().split()
    print(res)
    for i in res:
        if not 'абв' in i:
            print(i)