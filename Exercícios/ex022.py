#Crie um programa que leia o nome completo de uma pessaol e mostre:
#O nome comtodas as letras maiúsculas
#O nome com todas as letras minúsculas
#quantas letras tem sem contar com os espaços
#quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome: {}'.format(nome))
print('Analisando seu nome...')
print('Nome maiúsculo: {}'.format(nome.upper()))
print('Nome minúsculo: {}'.format(nome.lower()))
print('Quantas letras tem no nome: {}'.format(len(nome) - nome.count(' ')))
print('Quantas letras tem no primeiro nome: {}'.format(nome.find(' ')))