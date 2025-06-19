#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
print('-=-=-=CADASTRO-=-=-=-=')
pessoas = pessoas18 = homens = mulheres20 =0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in ['F', 'M'] :
        sexo = str(input('Sexo [F/M]'))[0].strip().upper()
    pessoas += 1
    if idade >= 18:
        pessoas18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres20 += 1
    continuar = ' '
    while continuar not in ['S','N']:
        continuar = str(input('Quer continuar [S/N]'))[0].strip().upper()
    if continuar == 'N':
        break
print(f"""Foram cadastradas {pessoas} pessoas entre elas estão {pessoas18} maiores de 18 anos, 
{homens} homens e {mulheres20} mulheres menores de 20 anos.""")
6