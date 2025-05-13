#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import random,shuffle
an1 = str(input('Primeiro aluno: '))
an2 = str(input('Segundo aluno: '))
an3 = str(input('Terceiro aluno: '))
an4 = str(input('Quarto aluno: '))
lista = [an1,an2,an3,an4]
shuffle(lista)
print('A ordem de apresentação')
print(lista)
