def log(primer, result):

    with open('logger.txt', 'a') as file:
        rasparse = ''.join(map(str, primer))
        rasparse = rasparse + '='
        result = str(result) + ';\n'
        file.write(str(rasparse))
        file.write(str(result))
       