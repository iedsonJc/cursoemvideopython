#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
# errado, peça a digitação novamente até ter um valor correto.
print('-=-=-=-=Analisando Dados-=-=-=-=-=')
nome = str(input('Nome: '))
idade = int(input('Idade: '))
sexo = ''
var = ''
while sexo not in ['M', 'F']:
     sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
     if sexo not in ['M', 'F']:
         print('Opção invalidade')
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print("Seu nome é {} da idade de {} do sexo {}".format(nome, idade, sexo))