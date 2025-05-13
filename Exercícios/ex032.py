#faça um programa que leia uma ano e diga se ele é um ano bissexto
print('====='*10)
ano = int(input('Qual ano você esta: '))
print('Você esta no ano {}?'.format(ano))
if ano % 2 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))