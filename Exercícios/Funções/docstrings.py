#docstrings
def contador(i, f, p):
    """faz uma contagem e mostra na tela
    :param i:inicio da contagem
    :param f: fim da contagem
    :param p: o passo da contagem
    :return: sem retorno
    função feita por iêdson luiz
    """
    c=i
    while c<=f:
        print(f'{c}',end='..')
        c +=p
    print('fim')


contador(1,10,2)
help(contador)


#parametros
def soma(a=0, b=0, c=0):
    """faz a soma de três valores
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    feito por iêdson
    """

    s = a + b + c
    print(f'A soma vale {s}')


soma(2, 4,8)
soma()

#variavel global e local
def test():
    # se acrescentamos 'global n1' a varivale local passa a ser global
    n1 = 4 #local
    print(f'N1 dentro vale {n1}')


n1 = 6 #global
test()
print(f'N1 fora vale {n1}')


#retun
def retorno(a=0,b=0,c=0):
    s = a + b + c
    return  s


r1 = retorno(3,4,5)
r2 = retorno(6, 8)
r3 = retorno(7)
print(f'Os resultados foram {r1}, {r2}, {r3}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *=c
    return f
f1 = fatorial(5)
f2 = fatorial(8)
f3 = fatorial()
print(f'O fatorial de 5={f1} 8={f2} 1={f3}')
n = int(input('Digite um número: '))
print(f'O farotrial de {n} é {fatorial(n)}')


def par(n=0):
    if n  % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um valor: '))
if par(num):
    print(f'{num} é par!')
else:
    print(f'{num} não é par!')