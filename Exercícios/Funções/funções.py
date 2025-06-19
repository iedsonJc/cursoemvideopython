#Nessa aula, vamos aprender o que são funções ou rotinas e como
#utilizar funções em Python. Funções são trechos de código que
#podem ser executados em momentos diferentes de nossos códigos em
#Python. Veja como funciona o comando def em Python e como utilizá-lo
#com parâmetros simples e múltiplos.
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    
def contador(* num):


# funçõe título
titulo('      Aprendendo funções')
titulo('           Python')

# funçõe soma
soma(7, 2)
soma(b=4, a=5) #alterando as posições de A e B

#função contador
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)



