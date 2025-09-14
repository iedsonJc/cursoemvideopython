def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0:31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)


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
