#Exercício Python 68: Faça um programa que jogue par ou ímpar com
# o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que
# ele conquistou no final do jogo
from random import  randint
print('-=-=-=-=-=Par ou Impar-=-=-=-=-=')
print('Vamos jogar par ou impar!')
contv = 0
while True:
    computador = randint(0, 11)
    jogador = int(input('Digite um valor: '))
    total = jogador + computador
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=(' '))
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if parouimpar == 'P':
        if total % 2 == 0:
            print('Você Venceu!!!')
            contv += 1
        else:
            print('Você perdeu!')
            break
    elif parouimpar == 'I':
        if total % 2 != 0:
            print('Você Venceu!')
            contv += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos Jogar novamente!')
print(f'GAME OVER,Você venceu {contv} vezes.')
