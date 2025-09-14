#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
#retornar um dicionário com as seguintes informações:
def notas(*num, sit=False):
    """
    fução para analisar a situação de um aluno
    :param num: uma ou mais notas de um aluno(aceita varias)
    :param sit: condição de situação de um aluno(opcional)
    :return: retorna a situação de um aluno
    """
    r = dict()
    r['total'] = len(num)
    r['menor'] = min(num)
    r['maior'] = max(num)
    r['média'] = sum(num)/len(num)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média']  >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


res = notas(3.5, 6.7, 9, sit=True)
print(res)