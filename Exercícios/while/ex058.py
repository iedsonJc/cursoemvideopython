#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
#agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('Escolha um número entre 0 e 10')
computador = randint(0,10)
acertou = False
tentativas = 1
while not acertou:
    jogador = int(input('{}ª tentativa: '.format(tentativas)))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maior...tente mais uma vez....')
        else:
            print('Menor....tente mais uma vez.......')
        tentativas += 1
print('Com {} tentativas'.format(tentativas))
print('Você acertou o computador escolheu {} e você {}'.format(computador, jogador))

