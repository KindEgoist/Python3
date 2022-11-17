def log(data):
    stroka = ""
    with open('tel1.txt', 'a') as file:
        for v in data.values():
            stroka += str(v) + ','
        stroka = stroka[:-1] + ';'
        file.write(stroka)
    with open('tel2.txt', 'a') as file:
        for v in data.values():
            stroka = str(v) + '\n'
            file.write(stroka)
        file.write('\n')
