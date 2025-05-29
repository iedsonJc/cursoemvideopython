# maior idade
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 7):
    ano = int(input('Qual ano você nasceu: '))
    if atual - ano >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Quantidades de pessoas que são menor de idade: {}'.format(menor))
print('Quantidades de pessoas que são maior de idade: {}'.format(maior))