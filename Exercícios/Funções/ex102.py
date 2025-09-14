#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois
#parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor
#lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=''):
    """
    Realiza o fatorial de um número mostrando na tela o resultado
    :param num: número a ser realizado o fatorial
    :param show: é a condicional para mostrar o calculo ou não.
    :return:
    """
    f = 1
    while True:
        show = str(input('Quer cálculo? [S/N]: ')).strip().upper()
        if show == 'S':
            for c in range(num, 0, -1):
                f *= c
                print(f'{c} ',end='')
                if c > 1:
                    print('x', end=' ')
                else:
                    print('=', end=' ')
            print(f)
            break
        else:
            for c in range(num, 0, -1):
                f *= c
            print(f'O fatorial de  {num} é {f}')
            break

print('Calculo de Fatorial')
num = int(input('Digite o valor: '))
fatorial(num,'')