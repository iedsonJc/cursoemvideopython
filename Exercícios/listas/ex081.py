#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
print('-=-'*15)
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    res = ' '
    while res not in ['S','N']:
        res = str(input('Quer continuar [S/N]: ')).upper().strip()
    if res == 'N':
        break
print('-=-'*15)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ondem decrescente {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista!.')
else:
    print('O número 5 não foi encontrado.')
print('-=-'*15)