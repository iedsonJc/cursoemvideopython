#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
print('-=-=-=ANALISANDO DADOS-=-=-=-=-')
somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhermenor = 0
mediaidade = 0
for p in range(1, 6):
    print('---------{}ª pessoa---------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if p ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem : idade

    if sexo in 'Ff' and idade < 20 :
        mulhermenor += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho é {} e tem {} anos'.format(nomevelho, mediaidade))
print('Ao todo são {} mulher com menos de 20 anos'.format(mulhermenor))