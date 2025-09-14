#Exercício Python 099: Faça um programa que tenha uma
#função chamada maior(), que receba vários parâmetros com
#valores .inteiros. Seu programa tem que analisar todos os
#valores e dizer qual deles é o maior.

def maior(* num):
    cont = maior = 0
    print('-=-'*15)
    print('\nAnalisando todos os valores:', end=' ')
    for valor in num:
        print(f'{valor} ', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informado {cont} valores.')
    print(f'O maior valor entre eles número é: {maior}')
    print()

maior(4, 6, 7, 3, 9)
maior( 5, 2, 4, 8)
maior(10, 1, 0)
print('-=-'*7,'FIM', '-=-'* 7)