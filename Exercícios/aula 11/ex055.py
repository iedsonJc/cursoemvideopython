#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
print('-=-=-=-=-=LEITOR DE PESO-=-=-=-=-=')
menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input('Qual peso da {}ª Kg: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))


