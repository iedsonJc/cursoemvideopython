#Exercício Python 085: Crie um programa onde o usuário
#possa digitar sete valores numéricos e cadastre-os em uma lista
#única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
print('-=-'*20)
lista = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite valor {c}: '))
    if valor % 2 == 0: #se é par vai ser adicionado
        lista[0].append(valor) #sera adicionado lista[0]
    else:
        lista[1].append(valor) #sera adicionado lista[1]
print('-=-'*20)
lista[0].sort()
lista[1].sort()
print(f'Lista completo {lista}')
print(f'Lista de números pares {lista[0]}')
print(f'Lista de números imapares {lista[1]}')


