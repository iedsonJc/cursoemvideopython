#Exercício Python 089: Crie um programa que leia nome e duas notas
#de vários alunos e guarde tudo em uma lista composta. No final,
#mostre um boletim contendo a média de cada um e permita que o
#usuário possa mostrar as notas de cada aluno individualmente.

print(f'{"BOLETIM DOS ALUNOS":>30}')
ficha = []
while True: #faz o soteio automatico
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) #adiciona os dados dos alunos

    resp = ' '
    while resp not in ['S', 'N']: #pergunta se quer cadastra mais alunos
        resp = str(input('Quer cadastrar mais um aluno?[S/N]')).strip().upper()
    if resp == 'N':
        break
print('-=-'*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') #estrutura de como os dados serão mostrados
print('-'*30)
for i, a in enumerate(ficha): #mostra os dados enumerando-os
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = ''
    while opc not in ['S','N']: #pergunta se quer mostrar as notas
        opc = str(input('Quer mostrar notas de algum aluno? [S/N]: ')).strip().upper()
    if opc == 'S':
        aluno = 0
        while aluno >= len(ficha)-1:#seleciona o aluno pelo indice
            aluno = int(input('Qual aluno? '))
            if aluno <= len(ficha)-1: #mostra as notas
                print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}')
                break
    if opc == 'N':
        print('<<<<<FINALIZANDO............')
        break