#Nessa aula, vamos aprender o que são funções ou rotinas e como
#utilizar funções em Python. Funções são trechos de código que
#podem ser executados em momentos diferentes de nossos códigos em
#Python. Veja como funciona o comando def em Python e como utilizá-lo
#com parâmetros simples e múltiplos.
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

# funçõe título
titulo('      Aprendendo funções')
titulo('           Python')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

# funçõe soma
soma(7, 2)
soma(b=4, a=5) #alterando as posições de A e B


def lista(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


lista(2, 1, 7)
lista(8, 0)
lista(4, 4, 7, 6, 2)

def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def sm(* val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')


sm(5,2 )
sm(2, 9, 4)