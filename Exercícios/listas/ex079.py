#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
lista = list()
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adiconado!')
    else:
        print('não vou nadicionar, valor duplicado!')
    resp = ' '
    while resp not in ['S','N']:
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=-'*4,'Lista','-=-'*4)
lista.sort()
print(lista)