#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.
print('-=-'*20)
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = ' '
    while res not in ['S','N']:
        res = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if res == 'N':
        break

for n in lista:  #ou desse jeito   for i, v in enumerate(list):
    if n % 2 == 0:                  # if v % 2 == 0
        pares.append(n)             # pares.append(v)
    else:
        impares.append(n)          #  impares.append(v)
print('-=-'*20)
lista.sort()
print(f'A lista de forma ordenada: {lista}')
print(f'Os números pares da lista: {pares}')
print(f'Os números impares da lista: {impares}')