#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
print('-=-'*10)
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3): #elementos da linha
    for c in range(0, 3): #elementos da coluna
        matriz[l][c] = int(input(f'Digite valor {l,c} :')) #adiciona os elementos na linha e na coluna

print('-=-'*10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  #mostra os elementos nas linhas e nas colunas formatados na matriz
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos números pares é {spar}')
for l in range(0, 3): #a contagem  das linhas na terceira coluno
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3): #a contagem das colunas na segunda linha
    if c == 0:  #na primeira coluna
        mai += matriz[1][c]  #o maior recebe o valor da colana 1 e linha 2
    elif matriz[1][c] > mai: #faz a contagem do c=1 e c=2, e fazendo a verificação dos valores
        mai = matriz[1][c]

print(f'O maior número é {mai}')