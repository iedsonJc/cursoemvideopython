#Exercício Python 092: Crie um programa que leia nome, ano de
#nascimento e carteira de trabalho e cadastre-o (com idade) em um
#dicionário. Se por acaso a CTPS for diferente de ZERO, o
#dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa
#vai se aposentar.
from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['idade']+(cadastro['contratação'] + 35)-datetime.now().year
print('-=-'*15)
for k, v in cadastro.items():
    print(f' -{k} <--> {v}')