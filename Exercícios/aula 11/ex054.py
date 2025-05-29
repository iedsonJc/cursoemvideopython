#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
print('-=-=-=Peso-=-=-=-=-=')
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    if atual - ano <= 20:
        menor += 1
    else:
        maior += 1
print("""Das {} pessoas, {} menor de idade
e {} maior idade""".format(c, menor, maior))