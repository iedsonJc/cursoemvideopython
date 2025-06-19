#Exercício Python 094: Crie um programa que leia nome, sexo e idade
#de várias pessoas, guardando os dados de cada pessoa em um
#dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

print(f'{'\033[4:31mCADASTRO\033[m':>30}')
print('-=-'*15)
pessoas = dict()
cadastro = list()
soma = média = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO!Por favor digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    while True:
        resp = str(input('Quer cadastrar mais alguma pessoas[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=-' * 15)
print(f'A) Ao todo foram cadastrada {len(cadastro)} pessoas.')
média = soma / len(cadastro)
print(f'B) A média das idades é {média:5.2f} anos.')
print('C) As mulheres cadastradas foram:', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f' {p['nome']}', end='')
print()
print('D) A listagem de pessoas a cima da médida:', end='')
for p in cadastro:
    if p['idade'] >= média:
        print('   ',end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<<<<ENCERRADO>>>>>')
