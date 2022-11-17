import input_and_output

def impor():
    with open ('tel1.txt','r') as file:
        spisok = file.readline().replace(';', ',').split(',')
        spisok.pop()
        input_and_output.vivod_imp(spisok)

def impor2():
    with open ('tel1.txt','r') as file:
        spisok = file.readline().replace(';', ',').split(',')
        spisok.pop()
        return spisok

        
    
    
