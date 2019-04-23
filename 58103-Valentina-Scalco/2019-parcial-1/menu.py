from decimal_hexadecimal import conver
import os
def main():
    os.system('clear')
    print('\tConversion de DECIMAL a HEXADECIMAL')
    print('Ingrese un numero decimal')
    numdecimal = input('')
    hexa = a(numdecimal)
    if hexa.find(' ') == -1:
        print('El numero en hexadecimal es ',hexa)
        input('Presione una tecla para volver')
        main()
    else:
        print (hexa)
        input('Presione una tecla para volver')
        main()
def a(numdecimal):
    if numdecimal.isdigit() == False :
        return 'ERROR -Ingrese solo numeros'
    else:
        hexa = conver(int(numdecimal))    
    return hexa

main()