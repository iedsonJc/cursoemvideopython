#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from statistics import median_high


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)
#   return res if not formato else moeda(res)


def diminuir(preço=0, taxa=0, formato= False):
    res = preço - (preço * taxa/100)
    return res if formato is  False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')



def resumo(preço=0, taxaa=10, taxar=5 ):
    print('-=-'*10)
    print('Resumo'.center(25))
    print('-=-'*10)
    print(f'Preço Analisando: \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço, True)}')
    print(f'A metade do preço: \t{metade(preço,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa,True)}')
    print(f' {taxar}% de redução: \t{diminuir(preço,taxar, True)}')
    print('-'*30)