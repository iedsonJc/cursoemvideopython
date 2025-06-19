#listas diferente das tupulas, podem ser alteradas.
lanches = ['tv','relogio','radio','celular','geladeira']
valores = [8,2,5,4,4,9,0]

#adiciona um elemento no final da lista
lanches.append('tvbox')
print(lanches)
#adicona um elemento na posição que você escolher
lanches.insert(0,'roteador')

#apagar elementos de uma lista
del lanches[3]
#remove o elemento na posião indicada
lanches.pop()
lanches.pop(3)
lanches.remove('tv')
if 'tv'in lanches:
    lanches.remove('tv')
else:
    print('Não achei tv na lista')

#mostra os valores da posição 2 a 4
valores = list(range(2,4))


#organiza os valores
valores.sort()
#ordem inversa
valores.sort(reverse=True)

#perguntando valores de uma lista para um usuario e mostra na tela
num = list()
for cont in range(0, 5):
    valores.append(int(input('Digite uma valor: ')))
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

#quando um lista esta igualada a outra elas se ligam e o que
#for alterado em uma tb sera na outra
a = [2, 3, 4, 7]
b = a #ligação A e B se tornam a mesma coisa
b = a [:] #B recebe todos os elementos de A
b[2] = 8
#o valor 4 que esta na posição 2 sera alterado pelo 8
#nas duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

