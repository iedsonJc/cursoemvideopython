from random import randint
from time import sleep
itens = ['PEDRA','PAPEL','TESOURA']
computador = randint(0,2)
print('-=--'*4,'JOKEMPO','--=-'*4)
print("""Sua opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input('Escolha: '))
print('====JO=====')
sleep(0.70)
print('     ====KEM=====')
sleep(0.70)
print('          ====PO=====')
sleep(0.70)
print('Computador: {}{}{}'.format('\033[1:33m',itens[computador],'\033[m'))
sleep(0.70)
print('Jogador: {}{}{}'.format('\033[1:34m',itens[jogador],'\033[m'))
sleep(0.70)
if computador == 0:
    if jogador == 0:
        print('\033[1:34mEmpate\033[m')
    elif jogador == 1:
        print('\033[1:32mJogador ganhou!\033[m')
    elif jogador == 2:
        print('\033[1:31mComputador Ganhou!\033[m')
    else:
        print('Jogada Invalida')
elif computador == 1:
    if jogador == 0:
        print('\033[1:31mComputador Ganhou!\033[m')
    elif jogador == 1:
        print('\033[1:34mEmpate\033[m')
    elif jogador == 2:
        print('\033[1:32mJogador ganhou!\033[m')
    else:
        print('Jogada Invalida')
elif computador == 2:
    if jogador == 0:
        print('\033[1:32mJogador ganhou!\033[m')
    elif jogador == 1:
        print('\033[1:31mComputador Ganhou!\033[m')
    elif jogador == 2:
        print('\033[1:34mEmpate\033[m')
    else:
        print('Jogada Invalida')
print('-=-'*6,'FIM','-=-'*6)