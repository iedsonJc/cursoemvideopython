#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
print(f'{"CONSULTA DE APROVAÇÃO":^30}')
aluno = dict()
while True:
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

    if aluno['media'] >= 7:
        aluno['situação'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
    print('<<<'*15)
    for k, v in aluno.items():
        print(f'{k} {'=':>9} {v:>10}')
    print('<<<'*15)
    resp = ''
    while resp not in ['S','N']:
        resp = str(input('Quer fazer outra consulta? [S/N]: ')).upper().strip()
    if resp == 'N':
        print(f'{"FINALIZADO":^30}')
        break


