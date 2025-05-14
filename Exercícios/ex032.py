#faça um programa que leia uma ano e diga se ele é um ano bissexto
print('====='*10)
from datetime import date
ano = int(input('Qual ano você esta? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))