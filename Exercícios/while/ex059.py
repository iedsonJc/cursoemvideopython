#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
print('-=---=-Operações Matematicas')
n1 = int(input('Digite o 1ª valor: '))
n2 = int(input('Digite o 2ª valor: '))
menu = 0
while menu != 5:
    print('-=-=-=-=MENU-=-=-=-=-=')
    print("""Escolha a operação
    [1]SOMA
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA""")
    print('<------------------------->')
    menu = int(input('>>>>>Escolha qual opção: '))
    if menu == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} O maior e {}'.format(n1, n2, maior))
    elif menu == 4:
        print('====NOVOS NÚMEROS====')
        n1 = int(input('Digite 1ª valor: '))
        n2 = int(input('Digite 2ª valor: '))
    elif menu == 5:
        print('FINALIZANDO___---___---__-_-_-_----')
    else:
        print('Opção invalida')
    print('=-='*14)
    sleep(1.5)
print('-=-=-=-=-=-=OBRIGADO-=-=-=-=-=-=-=')