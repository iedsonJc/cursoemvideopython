#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

print('-=-=-=-=Plíndomo-=-=-=-=-=')
frase = str(input('Digite o que vocẽ quer analisar:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('{} é um políndromo'.format(frase))
else:
    print('{} não é um políndromo'.format(frase))