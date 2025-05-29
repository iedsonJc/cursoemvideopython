#conversor de números
from time import sleep
print('==='*8,'Conversor','==='*8)
num = int(input('Digite um número: '))
print('''Escolha a base de conversão:
\033[1:31m[1]binario
\033[1:34m[2]octal
\033[1:32m[3]hexadecimal\033[m''')
esc = int(input('Escolha: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)

if esc == 1:
    print('====CONVERTENDO {} PARA BINARIO......'.format(num))
    sleep(2)
    print('\033[1:31m RESULTADO: {}'.format(binario[2:]),'\033[m')
elif esc == 2:
    print('====CONVERTENDO {} PARA OCTAL......'.format(num))
    sleep(2)
    print('\033[1:34m RESULTADO: {}'.format(octal[2:]),'\033[m')
elif esc == 3:
    print('====CONVERTENDO {} PARA HEXADECIMAL......'.format(num))
    sleep(2)
    print('\033[1:32m RESULATADO: {}'.format(hexadecimal[2:]),'\033[m')
print('==='*8,'Fim','==='*8)