#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
#semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor
#numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    """
    leiaInt é uma copia do int(input) com o acrescimo de validação
    :param msg: recebe a mensagem que mostra para o usuario
    :return: valor
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0:31mERRO! {n} NÃO É UM NÚMERAL.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um nuḿero: ')
print(f'\033[0:32mVocê digitou o númeral: {n}\033[m')