#Exercício Python 095: Aprimore o desafio 93 para que ele funcione
# com vários jogadores, incluindo um sistema de visualização de
#detalhes do aproveitamento de cada jogador.
print(f'{'JOGO DE FUTEBOL':>25}')
dados = dict()
partidas = list()
time = list()
print('-=-'*15)
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    totp = int(input(f'   Quantas partidas {dados["nome"]} jogou? '))
    partidas.clear()
    for p in range(0, totp):
        partidas.append(int(input(f'Quantos gols na partida {p+1}?: ')))
    dados['gols'] = partidas[:] #faz uma copia de partidas para dados
    dados['total'] = sum(partidas) #soma os valores que estão em partidas
    time.append(dados.copy())
    print('-=-' * 15)
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!Responda apenas S ou N.')
    if resp == 'N':
        break
print('---'*15)
print('cod.', end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print('-=-'*15)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('---'*15)
while True:
    while True:
        res = str(input('Quer ver o um jogador especifico?[S/N]: ')).strip().upper()[0]
        if res == 'S':
            busca = int(input('Mostarar qual jogador?'))
            if busca >= len(time):
                print(f'ERRO!Não existe jogador com esse código {busca}')
            else:
                print(f' --LEVANTAMENTO DDO JOGADOR {time[busca]["nome"]} :')
                for i, g in enumerate(time[busca]['gols']):
                    print(f'   NO jogo {i+1} fez {g} gols.')
        if res in 'SN':
            break
        print('ERRO!Responda apenas S ou N.')
    if res == 'N':
        print('>>>>>FINALIZANDO<<<<<<<')
        break

