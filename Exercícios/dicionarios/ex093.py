#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
#nome do jogador e quantas partidas ele jogou. Depois vai ler a
#quantidade de gols feitos em cada partida. No final, tudo isso
#será guardado em um dicionário, incluindo o total de gols feitos
#durante o campeonato.

print(f'{'JOGO DE FUTEBOL':>25}')
dados = dict()
partidas = list()
dados['nome'] = str(input('Nomedo jogador: '))
totp = int(input(f'   Quantas partidas {dados['nome']} jogou? '))
for p in range(0, totp):
    partidas.append(int(input(f'Quantos gols na partida {p+1}?: ')))
dados['gols'] = partidas[:] #faz uma copia de partidas para dados
dados['total'] = sum(partidas) #soma os valores que estão em partidas
print('-=-'*15)
print(dados)
print('-=-'*15)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-=-'*15)
print(f'O jogador {dados['nome']} jogou {totp} partidas')
for i, v in enumerate(dados['gols']):
    print(f'   =>Na partida {i+1}, fez {v} gols.')
print(f'     O total de gols foi {dados['total']}.')
print('---'*15)