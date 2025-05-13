#crie uma um programa que mostra a sua porção inteira
from math import trunc
num = float(input('Digite um número: '))
print('Número digitado:{}'.format(num))
print('Aparte inteiro é: {}'.format(trunc(num)))
