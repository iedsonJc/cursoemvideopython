#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
#parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
#de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(jog='<desconhecido>', gols=0):
    """"""
    print('-=-'*3,'JOGADOR','-=-'*3)
    print(f'Nome: {jog}')
    print(f'Gols Marcados: {gols}')


n = str(input('Nome do Jogador: '))
g = str(input('Quantos gols:: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)