from datetime import date
print('==='*6,'Alistamento militar','==='*6)
idade = int(input('Qual a sua idade? '))
atual = date.today().year
if idade == 18:
    print('Esta na hora de se alistar')
elif idade < 18:
    ano = (18 - idade) + atual
    print('Você devera se alistar no ano {}'.format(ano))
else:
    ano = (18 - idade) + atual
    print('Você deveria ter se alistado no ano {}'.format(ano))
