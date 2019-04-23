def conver (numdecimal):
    division = numdecimal
    count = str(numdecimal)
    hexadecimal= ''
    cont = len (count)
    while cont != 0:
        resto = division % 16
        resultado1 = str (resto)
        division = int(division/16)
        if resto >= 10:
            if resultado1 == '10':
                resultado1 = 'A'
            if resultado1 == '11':
                resultado1 = 'B'   
            if resultado1 == '12':
                resultado1 = 'C'
            if resultado1 == '13':
                resultado1 = 'D'  
            if resultado1 == '14':
                resultado1 = 'E'
            if resultado1 == '15':
                resultado1 = 'F'  
        if division == 0:
            cont = 1
        hexadecimal += resultado1
        cont -=1
    result = hexadecimal [::-1]
    return result
