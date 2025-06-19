#Exercício Python 091: Crie um programa onde 4 jogadores joguem um
#dado e tenham resultados aleatórios. Guarde esses resultados em um
#dicionário em Python. No final, coloque esse dicionário em ordem,
#sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import  sleep
from operator import  itemgetter
jogadores = {'jogador.1':randint(1, 6),
             'jogador.2':randint(1, 6),
             'jogador.3':randint(1, 6),
             'jogador.4':randint(1, 6),}
ranking = list()
print('Valores Sorteados:')
for k, v in jogadores.items():
    sleep(0.4)
    print(f'{k} tirou {v} no dado.')
    sleep(0.3)
    print(' ....',end='')
    sleep(0.3)
    print('........', end='')
    sleep(0.3)
    print('............', end='')
    sleep(0.3)
    print()
ranking = sorted(jogadores.items() ,key=itemgetter(1), reverse=True)
print('<<<<<<<<RANKING>>>>>>>>>')
for i, v in enumerate(ranking):
    sleep(0.4)
    print(f'  {i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(0.3)
    print('  ###', end='')
    sleep(0.3)
    print('  #########', end='')
    sleep(0.3)
    print('  ###########', end='')
    sleep(0.3)
    print()
print('>>>>>>>>FIM DE J0GO<<<<<<<<')