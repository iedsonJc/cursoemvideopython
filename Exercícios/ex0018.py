#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,radians,tan
an = float(input('Digite o valor do ângulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O ângulo é {}'.format(an))
print('O seu seno é {:.2f}'.format(seno))
print('O seu cosseeno é {:.2f}'.format(cosseno))
print('A sua tangente é {:.2f}'.format(tangente))
