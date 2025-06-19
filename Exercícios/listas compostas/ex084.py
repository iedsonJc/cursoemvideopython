#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
#mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


print('-=-'*20)
dados = []
pessoa = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoa) == 0: #se o tamanho total da lista é igual a 0
        mai = men = dados[1]
    else: #se o tamanho total da lista não for igual a 0
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    res = ' '
    while res not in ['S','N']:
        res = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

print(f'Ao todo foi cadastrado {len(pessoa)} pessoas.')
print(f'O menor peso foi {men}Kg: ',end=' ')
for p in pessoa: #vare a lista principal dividindo ela
    if p[1] == men:
        print(f'{[p[0]]}', end=' ')
print()
print(f'O menor peso foi {mai}Kg: ',end=' ')
for p in pessoa:
    if p[1] == mai:
        print(f'{[p[0]]}', end=' ')
print()