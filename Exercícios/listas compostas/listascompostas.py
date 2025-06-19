#listas compostas
#Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que
# permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

pessoas = [['iedson',28], ['artur',32], ['tiago',40], ['ieda',31]]

print(pessoas[0][0]) #iedson
print(pessoas[1][1]) #32
print(pessoas[2][0]) #tiago
print(pessoas[1])    #['iedson',28]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

########################################################

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])   #faz uma copia dos dados que foram imputado na lista dados para a lista galera
    dado.clear()             #apaga os dados da lista dados
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores é {totmen} menores de idade.')
