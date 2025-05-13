#cria um programa que leia o comprimento do cateto oposto e do cateto adjsente de um triângulo retângulo, e do comprinto da sua hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjasente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hypot(ca, co):.2f}')
print('A hipotenusa vai medir {:.2f}'.format(hi))