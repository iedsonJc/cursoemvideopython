#Ex088: Faça um programa que ajude um jogador da MEGA SENA a criar
#palpites.O programa vai perguntar quantos jogos serão gerados e
#vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
#tudo em uma lista composta.
from random import randint
from time import sleep
print('-=-'*12)
print('        MEGA SENA')
print('-=-'*12)
lista = []
megasena = []
jogada = []
totjogada = 1
contnum = 1
quantjogada = int(input('Quantos jogos você quer fazer: '))
while totjogada <= quantjogada:
    cont = 0
    while True: #faz o sorteio dos jogos
        sorteio = randint(1, 60)
        if sorteio not in lista: #so adiciona se o número sorteado não esta na lista
            lista.append(sorteio)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    megasena.append(lista[:])
    lista.clear()
    totjogada += 1

print('-=-'*12)
print(f'Resultados resultados:')
for i, l in enumerate(megasena): #mosta os números no formato 3x3
    print(f'Palpite {i+1}: {l}')
    sleep(1)
print('=-=-=-=-=-=< BOA SORTE! >-=-=-=-=-=-=')
