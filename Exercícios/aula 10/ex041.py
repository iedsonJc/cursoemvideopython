#confederação brasileira de Esportes
print('===Confederação brasileira de Natação===')
print('Classificação do atleta:')
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação do Atleta: Mirim')
elif idade <= 14:
    print('Classificação do Atleta: Infantil')
elif idade <= 19:
    print('Classificação do Atleta: Junior')
elif idade <= 25:
    print('Classificação do Atleta: Senior')
else:
    print('Classificação do Atleta: Master')
print('==='*5,'Fim','==='*5)
