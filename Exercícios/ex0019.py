#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
an1 = str(input('Primeiro aluno: '))
an2 = str(input('Segundo aluno: '))
an3 = str(input('Terceiro aluno: '))
an4 = str(input('Quarto aluno: '))
lista = [an1, an2, an3, an4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
